This is a project to test python imports in a nested package with tests.
The tests are in separate `test` folders in each submodule.

For the relative imports to work, the path to the project base directory has
 to be added to `sys.path`. This is achieved by calling

`python -m pycharm`

from `path/to/project`.

Project structure:

pythonimport

- __init__.py
- modA
  - __init__.py
  - one.py
  - two.py
  - test
    - test_a_one.py
    - test_a_two.py
- modB
  - __init__.py
  - one.py
  - two.py
  - test
    - test_b_one.py
    - test_b_two.py
