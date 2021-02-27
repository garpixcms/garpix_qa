
Garpix QA
=========

Checking the Django project for quality. It can be convenient if you include it in CI.

Used packages: 


* `django unittest <https://docs.djangoproject.com/en/3.1/topics/testing/overview/>`_ - unit testing in Django.
* `flake8 <https://pypi.org/project/flake8/>`_ - linter of source code.
* `radon <https://pypi.org/project/radon/>`_ - tool that computes various metrics from the source code.
* `bandit <https://pypi.org/project/bandit/>`_ - a security linter from PyCQA.

Quickstart
----------

Install with pip:

.. code-block:: bash

   pip install garpix_qa

Add the ``garpix_qa`` to your ``INSTALLED_APPS``\ :

.. code-block:: python

   # settings.py

   INSTALLED_APPS = [
       # ...
       'garpix_qa',
   ]

Check your project:

.. code-block:: bash

   python manage.py qa

Check your project with all logs:

.. code-block:: bash

   python manage.py qa --verbose

Example output with OK
^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   Input

     Directory: /Users/aleksejkuznecov/projects/garpix_packages/garpix-qa/backend
     Start at: 2021-02-27 12:09:30.999142

   Checking

     Checking style guide with flake8 (see ".flake8") OK
     Django unit tests OK
     Cyclomatic complexity with radon (see "radon.cfg") OK
     Security lint with bandit (only high-severity issues, see ".bandit") OK

   Result

     Problems found: 0
     End at: 2021-02-27 12:09:33.789880
     Duration: 0:00:02.790738

Example output with problems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   Input

     Directory: /Users/aleksejkuznecov/projects/garpix_packages/garpix-qa/backend
     Start at: 2021-02-27 12:23:41.066752

   Checking

     Checking style guide with flake8 (see ".flake8") ERROR
   /Users/aleksejkuznecov/projects/garpix_packages/garpix-qa/backend/garpix_qa/constants.py:18:4: W292 no newline at end of file
   /Users/aleksejkuznecov/projects/garpix_packages/garpix-qa/backend/garpix_qa/helpers.py:38:1: E302 expected 2 blank lines, found 1
   /Users/aleksejkuznecov/projects/garpix_packages/garpix-qa/backend/garpix_qa/colors.py:9:1: W391 blank line at end of file

     Django unit tests OK
     Cyclomatic complexity with radon (see "radon.cfg") OK
     Security lint with bandit (only high-severity issues, see ".bandit") ERROR
   [main]  INFO    Found project level .bandit file: /Users/aleksejkuznecov/projects/garpix_packages/garpix-qa/backend/.bandit
   [main]  INFO    profile include tests: None
   [main]  INFO    cli include tests: None
   [main]  INFO    cli exclude tests: None
   [main]  INFO    running on Python 3.8.2
   Run started:2021-02-27 12:23:45.044503

   Test results:
   >> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
      Severity: High   Confidence: High
      Location: /Users/aleksejkuznecov/projects/garpix_packages/garpix-qa/backend/garpix_qa/helpers.py:39
      More Info: https://bandit.readthedocs.io/en/latest/plugins/b602_subprocess_popen_with_shell_equals_true.html
   38      def shell_run(cmd):
   39          ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
   40          lines = ps.communicate()[0]

   --------------------------------------------------
   Code scanned:
           Total lines of code: 285
           Total lines skipped (#nosec): 0

   Run metrics:
           Total issues (by severity):
                   Undefined: 0.0
                   Low: 1.0
                   Medium: 0.0
                   High: 1.0
           Total issues (by confidence):
                   Undefined: 0.0
                   Low: 0.0
                   Medium: 0.0
                   High: 2.0
   Files skipped (0):


   Result

     Problems found: 2
     End at: 2021-02-27 12:23:45.098015
     Duration: 0:00:04.031263

Changelog
=========

See `CHANGELOG.md <CHANGELOG.md>`_.

Contributing
============

See `CONTRIBUTING.md <CONTRIBUTING.md>`_.

License
=======

`MIT <LICENSE>`_
