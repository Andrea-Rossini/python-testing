install:
	pip install --upgrade pip && pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py && pylint --disable=R,C test_app.py

test:
	python -m pytest -vv -cov= test_app.py
