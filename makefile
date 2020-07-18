# Author: Daniel Nicolas Gisolfi

repo=`grep -m 1 __title__ ./pytemplate/__version__.py | grep -o '"[^"]\+"' | cut -d '"' -f2`
version=`grep -m 1 __version__ ./pytemplate/__version__.py | grep -o '"[^"]\+"' | cut -d '"' -f2`
pypi_url=https://upload.pypi.org/legacy/

.PHONY: intro
intro:
	@echo "$(repo) v$(version)"

.PHONY: init
init:
	@python3 -m pip install pipenv 
	@python3 -m pipenv install --dev
	@echo "Now run: pipenv shell"

.PHONY: clean
clean:
	-rm -rf ./build ./dist ./__pycache__/
	-rm -rf ./$(repo)/$(repo).egg-info ./.eggs ./$(repo).egg-info
	-rm -f *.pyc *.pyo *.pyd *\$$py.class
	-find . -name "*.pyc" -exec rm -f {} \;
	-rm *.log
	-rm *.txt

.PHONY: test
test:
	@python3 -m pytest

.PHONY: build
build:
	-pipenv run pipenv-setup sync
	@python3 setup.py sdist bdist_wheel

.PHONY: install
install:
	@python3 -m pipenv run pipenv-setup sync
	@python3 -m pip install .

.PHONY: uninstall
uninstall:
	echo "python3 -m pip uninstall $(repo)==$(version) -y"
	@python3 -m pip uninstall $(repo)==$(version) -y

.PHONY: publish
publish: build
	@python3 -m twine upload --repository-url $(pypi_url) dist/*

.PHONY: pypi-install
pypi-install:
	@python3 -m pip install $(pypi_url)simple/ $(repo)==$(version)

.PHONY: sort
sort:
	isort -rc --atomic .
	# if this fails run pipenv shell and install dev
