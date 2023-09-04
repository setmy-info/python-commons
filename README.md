# python-commons

## Development

### Preparations

```shell
pip install -r requirements.txt
```

## Run unit tests

```shell
python -m unittest discover -s ./tests -p *_test.py
```

## Run integration tests

```shell
python -m unittest discover -s ./tests -p *_it.py
```

## Run behave (Cucumber) integration tests

```shell
behave
```
