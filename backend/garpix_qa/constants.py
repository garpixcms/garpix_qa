# flake8
CONFIG_FILE_NAME_FLAKE8 = '.flake8'
CONFIG_FILE_CONTENT_FLAKE8 = '''[flake8]
ignore = E501
exclude = .git,__pycache__,old,build,dist,venv,*/migrations/*,*/settings/*
max-complexity = 10
per-file-ignores = __init__.py: F401, F403
'''

# radon
CONFIG_FILE_NAME_RADON = 'radon.cfg'
CONFIG_FILE_CONTENT_RADON = '''[radon]
cc_min = C
'''

# bandit
CONFIG_FILE_NAME_BANDIT = '.bandit'
CONFIG_FILE_CONTENT_BANDIT = '''[bandit]
'''
