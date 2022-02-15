import sys
import io
import subprocess
from .colors import RESET
from .colors import GREEN
from .colors import RED
from .colors import BOLD
from django.test.utils import get_runner
from django.conf import settings


def print_default(text=''):
    sys.stdout.write(RESET)
    sys.stdout.write(f'  {text}')


def print_ok(lines='', verbose=False):
    sys.stdout.write(GREEN)
    sys.stdout.write(' OK\n')
    sys.stdout.write(RESET)
    if verbose:
        print(lines)


def print_error(lines=''):
    sys.stdout.write(RED)
    sys.stdout.write(' ERROR\n')
    sys.stdout.write(RESET)
    print(lines)


def print_header(text=''):
    sys.stdout.write(RESET)
    sys.stdout.write(BOLD)
    sys.stdout.write(f'\n{text}\n\n')


def print_empty():
    sys.stdout.write('\n')


def shell_run(cmd):
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  # nosec
    lines = ps.communicate()[0]
    lines = lines.decode("utf-8")
    return lines


def run_unit_tests(apps):
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    sys.stderr = new_stdout

    TestRunner = get_runner(settings)
    test_runner = TestRunner(keepdb=True)
    failures = test_runner.run_tests(apps)

    output = new_stdout.getvalue()

    sys.stderr = old_stderr
    sys.stdout = old_stdout

    return {
        "failures": failures,
        "output": output
    }
