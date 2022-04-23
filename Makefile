install:
	pip install -r requirements.txt
	python setup.py install

run:
	saganSat

refresh: install run

test:
	pytest -v --cov --cov-report=html:reports/html_dir --cov-report=xml:reports/coverage.xml --cov-report=term tests/

help:
	python setup.py --help-commands

uninstall:
	python setup.py uninstall
