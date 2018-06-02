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
	find . -name '*.log' -exec rm --force {} +


pip-base:
	pip install -U pip
	pip install pip-tools

pip-update: pip-base
	pip-compile -U -o requirements/requirements.txt requirements/requirements.in
	pip-compile -U -o requirements/requirements-dev.txt requirements/requirements-dev.in

pip-sync:
	pip-sync requirements/requirements-dev.txt

pip-dev:
	pip install ipython

pip: clean pip-sync pip-dev

isort:
	@pytest --isort  . > isort.log ; true


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


flake:
	@pytest --flake8 > flake8.log; true

prospector:
	@prospector > prospector.log; true

lint: isort flake prospector