from importlib.util import find_spec
from .helpers import shell_run
from .helpers import print_error
from .helpers import print_ok
from .helpers import run_unit_tests
from django.conf import settings
from .helpers import print_default
from .helpers import check_needed


def check_flake(directory: str, verbose: bool, config_file: str, all: bool, flake: bool, variables_passed: bool) -> int:
    if check_needed(all, flake, variables_passed):
        print_default(f'Checking style guide with flake8 (see "{config_file}")')
        backend_dir = directory
        cmd = f'flake8 {backend_dir}'
        lines = shell_run(cmd)
        if lines == '':
            print_ok(lines, verbose)
            return 0
        print_error(lines)
        return 1
    return 0


def check_radon(directory: str, verbose: bool, config_file: str, all: bool, radon: bool, variables_passed: bool) -> int:
    if check_needed(all, radon, variables_passed):
        print_default(f'Cyclomatic complexity with radon (see "{config_file}")')
        cmd = f'radon cc {directory}'
        lines = shell_run(cmd)
        if lines == '':
            print_ok(lines, verbose)
            return 0
        print_error(lines)
        return 1
    return 0


def check_security_linter(directory: str, verbose: bool, config_file: str, all: bool, linter: bool,
                          variables_passed: bool) -> int:
    if check_needed(all, linter, variables_passed):
        print_default(f'Security lint with bandit (only high-severity issues, see "{config_file}")')
        lines = shell_run(f'bandit -r {directory} -lll')
        if 'No issues identified' in lines:
            print_ok(lines, verbose)
            return 0
        print_error(lines)
        return 1
    return 0


def check_migrations(directory: str, verbose: bool, all: bool, migrations: bool, variables_passed: bool) -> int:
    if check_needed(all, migrations, variables_passed):
        print_default('Project migrations')
        cmd = f'python3 {directory}/manage.py makemigrations --check --dry-run'
        lines = shell_run(cmd)
        if 'No changes detected' in lines:
            print_ok(lines, verbose)
            return 0
        print_error(lines)
        return 1
    return 0


def check_unit_tests(directory: str, verbose: bool, all: bool, tests: bool, variables_passed: bool) -> int:
    if check_needed(all, tests, variables_passed):
        if find_spec('pytest') is not None:
            import re
            print_default('Django pytest')
            backend_dir = directory
            cmd = f'pytest {backend_dir}'
            lines = shell_run(cmd)
            tests_count: list = re.findall(r'collected (\d+) item', lines)
            passed_count: list = re.findall(r'(\d+) passed', lines)
            skipped_count: list = re.findall(r'(\d+) skipped', lines)

            if int(tests_count[0]) == sum(skipped_count + passed_count):
                print_ok(lines, verbose)
                return 0

            print_error(lines)
            return 1
        else:
            print_default('Django unit tests')
            failures, output = run_unit_tests(())

            if failures:
                print_error(output)
                return 1
            print_ok('', verbose)
            return 0
    return 0


def check_garpix_page_tests(verbose: bool, all: bool, garpix_page: bool, variables_passed: bool) -> int:
    if 'garpix_page' in settings.INSTALLED_APPS and check_needed(all, garpix_page, variables_passed):
        print_default('Django unit tests garpix_page')
        garpix_tests_result = run_unit_tests(('garpix_page',))

        if garpix_tests_result['failures']:
            print_error(garpix_tests_result['output'])
            return 1
        print_ok('', verbose)
    return 0


def check_lighthouse(verbose: bool = False, clear_reports: bool = False, all: bool = False) -> int:
    if all:
        print_default('Lighthouse CI')
        shell_run('lhci collect')
        lines = shell_run('lhci assert')
        if clear_reports:
            shell_run('rm -rf .lighthouseci')
        if 'Assertion failed' in lines:
            print_error(lines)
            return 1
        print_ok(lines, verbose)
    return 0
