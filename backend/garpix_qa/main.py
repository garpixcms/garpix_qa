import os
from .helpers import print_header
from .helpers import print_default
from .helpers import shell_run
from .helpers import print_error
from .helpers import print_ok
from .helpers import print_empty
import datetime
from .constants import CONFIG_FILE_NAME_FLAKE8, CONFIG_FILE_CONTENT_FLAKE8
from .constants import CONFIG_FILE_NAME_RADON, CONFIG_FILE_CONTENT_RADON
from .constants import CONFIG_FILE_NAME_BANDIT, CONFIG_FILE_CONTENT_BANDIT


def create_config(directory, config_file_name, config_file_content):
    path = os.path.join(directory, config_file_name)
    if not os.path.isfile(path):
        with open(path, 'w') as f:
            f.write(config_file_content)


def create_configuration_files(directory):
    create_config(directory, CONFIG_FILE_NAME_FLAKE8, CONFIG_FILE_CONTENT_FLAKE8)
    create_config(directory, CONFIG_FILE_NAME_RADON, CONFIG_FILE_CONTENT_RADON)
    create_config(directory, CONFIG_FILE_NAME_BANDIT, CONFIG_FILE_CONTENT_BANDIT)


def run_qa(directory, verbose=False):
    #
    os.chdir(directory)
    create_configuration_files(directory)
    #
    error_count = 0
    start_at = datetime.datetime.now()
    #
    print_header('Input')
    print_default(f'Directory: {directory}\n')
    print_default(f'Start at: {start_at}\n')

    print_header('Checking')

    # flake8 for backend
    print_default(f'Checking style guide with flake8 (see "{CONFIG_FILE_NAME_FLAKE8}")')
    backend_dir = directory
    cmd = f'flake8 {backend_dir}'
    lines = shell_run(cmd)
    if lines == '':
        print_ok(lines, verbose)
    else:
        print_error(lines)
        error_count += 1

    # Unit tests
    print_default('Django unit tests')
    cmd = f'python3 {directory}/manage.py test --keepdb'
    lines = shell_run(cmd)
    if 'OK' in lines:
        print_ok(lines, verbose)
    else:
        print_error(lines)
        error_count += 1

    # Cyclomatic complexity
    print_default(f'Cyclomatic complexity with radon (see "{CONFIG_FILE_NAME_RADON}")')
    cmd = f'radon cc {directory}'
    lines = shell_run(cmd)
    if lines == '':
        print_ok(lines, verbose)
    else:
        print_error(lines)
        error_count += 1

    # Security linter
    print_default(f'Security lint with bandit (only high-severity issues, see "{CONFIG_FILE_NAME_BANDIT}")')
    lines = shell_run(f'bandit -r {directory} -lll')
    if 'No issues identified' in lines:
        print_ok(lines, verbose)
    else:
        print_error(lines)
        error_count += 1

    # *** RESULT ***
    end_at = datetime.datetime.now()
    duration = end_at - start_at

    print_header('Result')
    print_default(f'Problems found: {error_count}\n')
    print_default(f'End at: {end_at}\n')
    print_default(f'Duration: {duration}\n')
    print_empty()
    if error_count > 0:
        exit(1)
