# get_wp
experimental fetch and manipulation of text from wikipedia

more focused on framework/ecosystem right now rather than content:

[git](https://git-scm.com/): source management  
[github](https://github.com): public remote source repository  
[pyenv](https://github.com/pyenv/pyenv): python version manager. lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.  
[poetry](https://python-poetry.org): manage Python packaging and dependencies. Its ease of  use and support for modern workflows make it the ideal successor to the  venerable setuptools. It is similar to npm and yarn in the JavaScript  world, and to other modern package and dependency managers. For alternatives to Poetry, have a look at flit, pipenv, pyflow, and dephell.  
[pytest](https://docs.pytest.org/en/latest/) unit test framework - somewhat of the de facto standard for python  
[nox](https://pypi.org/project/nox/) automates testing in multiple python environments
[flake8](https://pypi.org/project/flake8/) lint aggregator
[flake8-black](https://pypi.org/project/flake8-black/) flake8 plugin to run black code formatter from within the flake plugin ecosystem
[flake8-bugbear](https://pypi.org/project/flake8-bugbear/) flake8 plugin that finds likely bugs and design flaws
[flake8-import-order](https://pypi.org/project/flake8-import-order/) flake8 plugin that checks import ordering
[safety](https://github.com/pyupio/safety) check installed dependencies for know security vulnerabilities


# how-to notes
install homebrew
brew install git
brew install macvim
install iterm2

## initial git config
git config --global user.name Steve Rutledge
git config --global user.email 44811980+SteveRutledge@users.noreply.github.com

ssh-keygen -t rsa -b 4096 -C 'sterutle@gmail.com'
	copy contents of file ~/.ssh/id_rsa.pub and add under "SSH keys" 
	in github -> settings -> ssh and gpg keys

save passphrase in password manager!

$ git clone git@github.com:SteveRutledge/python_project_scaffold.git
cd python_project_scaffold

## install pyenv
curl https://pyenv.run | bash

## install pyenv dependencies
brew install readline xz

## what version of python are available?
pyenv install --list

## install
pyenv install 3.8.3
pyenv install 3.7.7

## make your fresh pythons available inside the project
pyenv local 3.8.3 3.7.7

## install poetry for managing python packing and dependencies
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

add to ~/.zshrc
	source ~/.poetry/env

## initialize project
poetry init --no-interaction
this will create a .toml file
    tom's obvious, minimal language
    used for a python project config file

## create managed env for your project, install your package into it, create .lock file
poetry install
poetry run python
the lock file tracks exact versions installed in virtual environment for this project

## add click package
poetry install click

## update to latest  minor update
poetry update click
major release changes must be explicit
poetry add click^7.0

## run package
poetry run get_wp
poetry run get_wp --help
poetry run get_wp -l de

## add requests package
poetry add requests

## add pytest package, but only as a development dependency
poetry add --dev pytest

## run pytest unit tests
poetry run pytest

## run pytest with code coverage analysis
poetry run pytest --cov

## install nox
pip install --user --upgrade nox

configure noxfile.py

## add mock support to pytest
poetry add --dev pytest-mock

##  run nox
nox 

##  reuse virtual envs
nox -r

## configure nox linting with flake8 using .flake config file
##  lint
nox -rs lint

# add blacken to nox
## blacken
nox -rs black

poetry add insecure-package
nox -rs safety
poetry remove insecure-package



# add nox flake8-import-order 

# add nox flake8-bugbear



lint
blacken 
