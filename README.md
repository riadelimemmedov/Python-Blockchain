
***Activate the virtual environment***

```
poetry shell
```

***Install all packages***

```
poetry install
```

***Get virtual environment path***

```
echo $VIRTUAL_ENV
```

***Run the tests***

Make sure to activate the virtual environment

```
python3 -m pytest -s backend/tests
```