# python-commons

## Development

### Preparations

```shell
# Win
py -3.14 -m venv ./.venv
# *nix
python -m venv ./.venv
# Win
.\.venv\Scripts\activate
# *nix
source ./.venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For developing depending on the project / module, dependency can be added into **requirements.txt** as:

    python-commons @ file:///C:/sources/setmy.info/submodules/python-commons

## Upgrade

```shell
pip install --upgrade behave pyyaml wheel twine pip_audit bandit
```

### PyCharm

"File" → "Settings" → Python Integrated Tools → Default test runner: Unittest

Running tests has a problem: a working directory has to be set for tests.

### Run unit tests

```shell
python -m unittest discover -s ./test/info/setmy
```

### Run integration tests

```shell
python -m unittest discover -s ./test/info/setmy -p it_*.py
```

### Run behave (Cucumber) integration tests

```shell
behave
```

### All tests

```shell
python -m unittest discover -s ./test/info/setmy && python -m unittest discover -s ./test/info/setmy -p it_*.py && behave
```

### Security Checks

The project uses popular Python security tools to ensure dependency safety and code quality.

#### Dependency Vulnerability Check (`pip-audit`)

This tool checks installed packages against known vulnerability databases (PyPI Advisory Database). It is the Python
equivalent of Java's dependency check.

**Run check:**

```sh
pip-audit -r requirements.txt
```

#### Static Analysis Security Testing (`bandit`)

Bandit is a tool designed to find common security issues in Python code.

**Run check:**

```sh
bandit -r smi_python_commons
```

### Update version info

```shell
# Win
set NAME=smi_python_commons
set VERSION=0.4.0
# *nix
NAME=smi_python_commons
VERSION=0.4.0
# Win
python smi_python_commons/scm_version.py %NAME% %VERSION%
# *nix
python smi_python_commons/scm_version.py ${NAME} ${VERSION}
git add ./${NAME}/project.py
git commit -m "project.py updated"
git push
```

## setup.py

`setup.py` is the **package distribution configuration** file. It makes this project an installable Python package that
can be:

- Built into a distributable artifact (`.whl` / `.tar.gz`)
- Installed locally via `pip install .`
- Published to PyPI (or a private registry)

### What each part does

| Field                      | Value                                             | Meaning                                 |
|----------------------------|---------------------------------------------------|-----------------------------------------|
| `name`                     | `NAME` from `project.py`                          | Package name on PyPI                    |
| `version`                  | `VERSION` from `project.py`                       | Package version                         |
| `packages=find_packages()` | auto-detected                                     | Includes all sub-packages               |
| `install_requires`         | `pyyaml`                                          | Runtime dependency                      |
| `extras_require[dev]`      | `bandit`, `behave`, `pip_audit`, `wheel`, `twine` | Dev/build tools (from requirements.txt) |

### How to use it

**Build the package:**

```shell
python setup.py sdist bdist_wheel
# or with modern tooling:
pip install build && python -m build
```

**Install locally (editable/dev mode):**

```shell
pip install -e .
```

**Install locally with dev dependencies:**

```shell
pip install -e .[dev]
```

**Install normally:**

```shell
pip install .
```

**Publish to PyPI:**

```shell
twine upload dist/*
```

> **Note:** `setup.py` is the legacy way (pre-PEP 517). Modern projects use `pyproject.toml` with
> `[build-system]` + `[project]` sections instead, but `setup.py` still works fine and is widely supported.

## Deploy

```shell
python setup.py sdist bdist_wheel
twine upload dist/*
git tag -a ${VERSION} -m "${VERSION}"
git push --tags
```

## Release

1. Update version info
2. Deploy

```shell
python setup.py sdist bdist_wheel && twine upload dist/*
```
