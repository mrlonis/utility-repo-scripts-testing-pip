# utility-repo-scripts-testing

## Installing Requirements

```shell
pip install -r requirements.txt
```

## Linting

```shell
flake8 src tests
pylint src tests
```

## Testing

```shell
pytest --cov=src tests/ -n auto
```
