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

# lighthouse
CONFIG_FILE_NAME_LIGHTHOUSE = 'lighthouserc.json'
CONFIG_FILE_CONTENT_LIGHTHOUSE = '''
{
  "ci": {
    "collect": {
      "url": "http://127.0.0.1:8000"
    },
    "assert": {
      "assertions": {
        "categories:performance": [
          "error",
          {
            "minScore": 0.90
          }
        ],
        "categories:accessibility": [
          "error",
          {
            "minScore": 0.90
          }
        ],
        "categories:best-practices": [
          "error",
          {
            "minScore": 0.90
          }
        ],
        "categories:SEO": [
          "error",
          {
            "minScore": 0.90
          }
        ]
      }
    }
  }
}
'''
