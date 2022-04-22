install:
	pip install -r requirements.txt
	python setup.py install

run:
	saganSat

refresh: install run

test:
	pytest -v tests/

help:
	python setup.py --help-commands

uninstall:
	python setup.py uninstall
