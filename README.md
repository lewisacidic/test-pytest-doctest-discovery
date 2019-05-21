# Test PyTest Doctest Discovery

A minimal example of pytest doctest discovery, used to highlight a requested functionality of VSCode-python (as of version 2019.4.12954).

## Installing

Run

```sh
pip install -r requirements.txt
```

## Running Tests

Running from the command line:

```sh
pytest
========================== test session starts ===========================
platform linux -- Python 3.7.3, pytest-4.4.1, py-1.8.0, pluggy-0.9.0
rootdir: /home/rich/git/test-pytest-doctest-discovery, inifile: pytest.ini
plugins: flake8-1.0.4, cov-2.6.1
collected 5 items                                                                                                                                                                              

docs/index.md .                                                                                                                                                                          [ 20%]
example/example.py .                                                                                                                                                                     [ 40%]
example/test_example.py ...                                                                                                                                                              [100%]

======================== 5 passed in 0.04 seconds ========================
```

Collects 5 tests: 3 in `example/test_example.py` (the unit tests), 1 in `example/example.py` (the module doctest), 1 in `docs/index.md` the markdown doctest.

In Visual Studio Code, run `Discover Tests`, then run tests.
This finds and runs 4 tests (the markdown doctest is not found) in the bottom bar.

Going to the Test Explorer, only the 3 unit tests are listed.

Ideally, all would be found, and would appear in the Test Explorer.
