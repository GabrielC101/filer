TEST_PATH=./

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +

clean:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info
	rm --force --recursive *.egg
	rm --force --recursive .mypy_cache/
	rm --force --recursive docs/_build/
	rm --force --recursive .cache
	rm --force --recursive .coverage
	rm --force --recursive .tox
	rm --force --recursive .pytest_cache
	find . -name '__pycache__' -exec rm --recursive --force {} +


pip: clean pip-compile pip-sync

isort:
	isort --skip-glob=.tox --recursive --check-only . &> isort.log

lint:
	flake8 --exclude=.tox

test: clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)

tox: clean
	pip install pytest mock coverage tox
	tox .

build: clean
	python setup.py bdist_wheel --universal

upload: build
	twine upload -r pypitest dist/thicket-*
	twine upload -r pypi dist/thicket-*


deploy: clean build upload
