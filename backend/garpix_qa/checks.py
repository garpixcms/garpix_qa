from importlib.util import find_spec
from .helpers import shell_run
from .helpers import print_error
from .helpers import print_ok
from .helpers import run_unit_tests
from django.conf import settings
from .helpers import print_default


def check_flake(directory, verbose, config_file):
    print_default(f'Checking style guide with flake8 (see "{config_file}")')
    backend_dir = directory
    cmd = f'flake8 {backend_dir}'
    lines = shell_run(cmd)
    if lines == '':
        print_ok(lines, verbose)
        return 0
    print_error(lines)
    return 1


def check_radon(directory, verbose, config_file):
    print_default(f'Cyclomatic complexity with radon (see "{config_file}")')
    cmd = f'radon cc {directory}'
    lines = shell_run(cmd)
    if lines == '':
        print_ok(lines, verbose)
        return 0
    print_error(lines)
    return 1


def check_security_linter(directory, verbose, config_file):
    print_default(f'Security lint with bandit (only high-severity issues, see "{config_file}")')
    lines = shell_run(f'bandit -r {directory} -lll')
    if 'No issues identified' in lines:
        print_ok(lines, verbose)
        return 0
    print_error(lines)
    return 1


def check_migrations(directory, verbose):
    print_default('Project migrations')
    cmd = f'python3 {directory}/manage.py makemigrations --check --dry-run'
    lines = shell_run(cmd)
    if 'No changes detected' in lines:
        print_ok(lines, verbose)
        return 0
    print_error(lines)
    return 1


def check_unit_tests(directory, verbose):
    if find_spec('pytest') is not None:
        import re
        print_default('Django pytest')
        backend_dir = directory
        cmd = f'pytest {backend_dir}'
        lines = shell_run(cmd)
        tests_count = re.findall(r'collected (\d+) item', lines)
        passed_count = re.findall(r'(\d+) passed', lines)
        if len(tests_count) == 1 and len(passed_count) == 1 and tests_count[0] == passed_count[0]:
            print_ok(lines, verbose)
            return 0
        print_error(lines)
        return 1
    else:
        print_default('Django unit tests')
        tests_result = run_unit_tests(())

        if tests_result['failures']:
            print_error(tests_result['output'])
            return 1
        print_ok('', verbose)
        return 0


def check_garpix_page_tests(verbose):
    if 'garpix_page' in settings.INSTALLED_APPS:
        print_default('Django unit tests garpix_page')
        garpix_tests_result = run_unit_tests(('garpix_page',))

        if garpix_tests_result['failures']:
            print_error(garpix_tests_result['output'])
            return 1
        print_ok('', verbose)
    return 0
