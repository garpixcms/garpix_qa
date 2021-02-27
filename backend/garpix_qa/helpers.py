import sys
import subprocess
from .colors import RESET
from .colors import GREEN
from .colors import RED
from .colors import BOLD


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
