# python-commons

## Development

### Preparations

```shell
pip install -r requirements.txt
```

### Run unit tests

```shell
python -m unittest discover -s ./tests
```

### Run integration tests

```shell
python -m unittest discover -s ./tests -p it_*.py
```

### Run behave (Cucumber) integration tests

```shell
behave
```
