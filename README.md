# python-commons

## Development

### Preparations

```shell
pip install -r requirements.txt
```

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

### PyCharm

Running tests have a problem: working directory have to be set for tests

## Deploy

```shell
python setup.py sdist bdist_wheel
twine upload dist/*
```
