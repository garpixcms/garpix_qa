import os

from .helpers import print_header
from .helpers import print_default
from .helpers import print_empty

from .checks import check_flake
from .checks import check_radon
from .checks import check_security_linter
from .checks import check_migrations
from .checks import check_unit_tests
from .checks import check_garpix_page_tests

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
    error_count += check_flake(directory, verbose, CONFIG_FILE_NAME_FLAKE8)

    # Cyclomatic complexity
    error_count += check_radon(directory, verbose, CONFIG_FILE_NAME_RADON)

    # Security linter
    error_count += check_security_linter(directory, verbose, CONFIG_FILE_NAME_BANDIT)

    # Project migrations
    error_count += check_migrations(directory, verbose)

    # Unit tests
    error_count += check_unit_tests(directory, verbose)

    # Unit tests garpix_page
    error_count += check_garpix_page_tests(verbose)

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
