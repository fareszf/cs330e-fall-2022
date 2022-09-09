#!/usr/bin/env python3

# ------------
# Coverage1.py
# ------------

# https://coverage.readthedocs.org

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(1), 1)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
$ coverage help
Coverage.py, version 5.1 with C extension
Measure, collect, and report on code coverage in Python programs.

usage: coverage <command> [options] [args]

Commands:
    annotate    Annotate source files with execution information.
    combine     Combine a number of data files.
    erase       Erase previously collected coverage data.
    help        Get help on using coverage.py.
    html        Create an HTML report.
    json        Create a JSON report of coverage results.
    report      Report coverage stats on modules.
    run         Run a Python program and measure code execution.
    xml         Create an XML report of coverage results.

Use "coverage help <command>" for detailed help on any command.
Full documentation is at https://coverage.readthedocs.io



$ coverage help run
Usage: coverage run [options] <pyfile> [program options]

Run a Python program, measuring code execution.

Options:
  -a, --append          Append coverage data to .coverage, otherwise it starts
                        clean each time.
  --branch              Measure branch coverage in addition to statement
                        coverage.
  --concurrency=LIB     Properly measure code using a concurrency library.
                        Valid values are: thread, gevent, greenlet, eventlet,
                        multiprocessing.
  --context=LABEL       The context label to record for this coverage run.
  --include=PAT1,PAT2,...
                        Include only files whose paths match one of these
                        patterns. Accepts shell-style wildcards, which must be
                        quoted.
  -m, --module          <pyfile> is an importable Python module, not a script
                        path, to be run as 'python -m' would run it.
  --omit=PAT1,PAT2,...  Omit files whose paths match one of these patterns.
                        Accepts shell-style wildcards, which must be quoted.
  -L, --pylib           Measure coverage even inside the Python installed
                        library, which isn't done by default.
  -p, --parallel-mode   Append the machine name, process id and random number
                        to the .coverage data file name to simplify collecting
                        data from many processes.
  --source=SRC1,SRC2,...
                        A list of packages or directories of code to be
                        measured.
  --timid               Use a simpler but slower trace method. Try this if you
                        get seemingly impossible results!
  --debug=OPTS          Debug options, separated by commas. [env:
                        COVERAGE_DEBUG]
  -h, --help            Get help on this command.
  --rcfile=RCFILE       Specify configuration file. By default '.coveragerc',
                        'setup.cfg', 'tox.ini', and 'pyproject.toml' are
                        tried. [env: COVERAGE_RCFILE]

Full documentation is at https://coverage.readthedocs.io



$ coverage help report
Usage: coverage report [options] [modules]

Report coverage statistics on modules.

Options:
  --contexts=REGEX1,REGEX2,...
                        Only display data from lines covered in the given
                        contexts. Accepts Python regexes, which must be
                        quoted.
  --fail-under=MIN      Exit with a status of 2 if the total coverage is less
                        than MIN.
  -i, --ignore-errors   Ignore errors while reading source files.
  --include=PAT1,PAT2,...
                        Include only files whose paths match one of these
                        patterns. Accepts shell-style wildcards, which must be
                        quoted.
  --omit=PAT1,PAT2,...  Omit files whose paths match one of these patterns.
                        Accepts shell-style wildcards, which must be quoted.
  -m, --show-missing    Show line numbers of statements in each module that
                        weren't executed.
  --skip-covered        Skip files with 100% coverage.
  --skip-empty          Skip files with no code.
  --debug=OPTS          Debug options, separated by commas. [env:
                        COVERAGE_DEBUG]
  -h, --help            Get help on this command.
  --rcfile=RCFILE       Specify configuration file. By default '.coveragerc',
                        'setup.cfg', 'tox.ini', and 'pyproject.toml' are
                        tried. [env: COVERAGE_RCFILE]

Full documentation is at https://coverage.readthedocs.io



$ coverage run --branch Coverage1.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



$ coverage report -m
Name           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------
Coverage1.py      16      4      4      1    65%   15-19, 14->15
"""