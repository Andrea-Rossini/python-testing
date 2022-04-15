# python-testing
This is a simple repo for debugging python code

## Initial project setup

1. Install virtual environment

```console

pip install virtualenv

python -m virtualenv .python-testing

source .python-testing/bin/activate VENV
```

2. Create files
```console

touch Makefile

touch requirements.txt

touch app.py

touch test_app.py
```

3. Edit requirements.txt
```console
pylint
pytest
```

4. Edit Makefile
```console
install:
	pip install --upgrade pip && pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py && pylint --disable=R,C test_app.py

test:
	python -m pytest -vv -cov= test_app.py
	
pipeline:
	install
	lint
	test
```
# Continuous Delivery with GitHub Actions
Once written app.py and test_app.py, is possible to build a continuous delivery system that checks for every PUSH the code uploaded. Check the .yaml file in this repo as an example.
