# get_wp

[![Tests](https://github.com/SteveRutledge/get_wp/workflows/Tests/badge.svg)](https://github.com/SteveRutledge/get_wp/actions)
[![Codecov](https://codecov.io/gh/SteveRUtledge/get_wp/branch/master/graph/badge.svg)](https://codecov.io/gh/SteveRutledge/get_wp)
[![Read the Docs](https://readthedocs.org/projects/get_wp/badge/)](https://get_wp.readthedocs.io/)
Experimental fetch and manipulation of text from wikipedia.

I am more focused on SDLC framework/ecosystem right now rather than content:

summary:<br/>
    * manage your source in a distributed fashion<br/>
    * across multiple versions of python<br/>
    * with a framework for project packaging and package dependencies<br/>
    * and a framework for unit tests<br/>
    * and code coverage analysis<br/>
    * automated testing, ci and cd across multiple environments<br/>
    * lint check for code style, likely bugs, design flaws, import order<br/>
    * document code in-place, while checking for docstring standards conformance<br/>
    * generate html docs from docstrings<br/>
    * check dependencies for known security vulnerabilities<br/>
    * decorate code with type annotations, then use for static and runtime type checking<br/>
    * auto-format code on pre-commit<br/>
    * test that docstrings match code and docstring examples match example output<br/>
    * track status of ci tests and doc tests with dashboard badges<br/>
    * automatically create release notes<br/>
    * publish to a package repository for easy deployments/updates<br/>
    * publish versioned docs to a document repository, auto-rebuilt on project update<br/>

[git](https://git-scm.com/): source management.<br/>
[github](https://github.com): public remote source repository.<br/>
[pyenv](https://github.com/pyenv/pyenv): python version manager. lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well..<br/>
[poetry](https://python-poetry.org): manage Python packaging and dependencies. Its ease of  use and support for modern workflows make it the ideal successor to the  venerable setuptools. It is similar to npm and yarn in the JavaScript  world, and to other modern package and dependency managers. For alternatives to Poetry, have a look at flit, pipenv, pyflow, and dephell..<br/>
[pytest](https://docs.pytest.org/en/latest/) unit test framework - somewhat of the de facto standard for python.<br/>
[nox](https://pypi.org/project/nox/): automates testing in multiple python environments.<br/>
[flake8](https://pypi.org/project/flake8/): lint aggregator.<br/>
[flake8-black](https://pypi.org/project/flake8-black/): flake8 plugin to run black code formatter from within the flake plugin ecosystem.<br/>
[flake8-bugbear](https://pypi.org/project/flake8-bugbear/): flake8 plugin that finds likely bugs and design flaws.<br/>
[flake8-import-order](https://pypi.org/project/flake8-import-order/): flake8 plugin that checks import ordering.<br/>
[flake8-docstrings](https://gitlab.com/pycqa/flake8-docstrings): check that docstrings are compliant with pep 257 style recommendations..<br/>
[safety](https://github.com/pyupio/safety): check installed dependencies for know security vulnerabilities.<br/>
[pre-commit](https://pre-commit.com/): python framework for git pre-commit hooks.<br/>
[mypy](http://mypy-lang.org/): static type checker, uses type annotations and inference to verify type correctness without running program
[pytype](https://google.github.io/pytype/): another static type checker.<br/>
[marshmallow](https://marshmallow.readthedocs.io/): define schemas to serialize, deserialize and validate data.<br/>
[desert](https://desert.readthedocs.io/): use type annotations of dataclasses to generate serialization schemas for them.<br/>
[typeguard](https://github.com/agronholm/typeguard): runtime type checker for python, when it is impractical or impossible to strictly type a static code path.<br/>
[darglint](https://github.com/terrencepreilly/darglint): check that docstrings match function definitions.<br/>
[sphinx](http://www.sphinx-doc.org/): generate documentation.<br/>
[autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html): enables Sphinx to generate API documentation from the docstrings in your package.<br/>
[napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html): pre-processes Google-style docstrings to reStructuredText.<br/>
[sphinx-autodoc-typehints](https://github.com/agronholm/sphinx-autodoc-typehints): uses type annotations to document the types of function parameters and return values.<br/>
[releaseDrafter](https://github.com/release-drafter/release-drafter): drafts your next release notes as pull requests are merged into master.<br/>
[codecov](https://codecov.io/): code coverage reporting service.<br/>
[readthedocs](https://readthedocs.org/): hosting service for documentation, rebuilds on project update, versioned docs.<br/>

### how-to notes

    #install homebrew
    brew install git
    brew install macvim
    install iterm2

    #initial git config
    git config --global user.name Steve Rutledge
    git config --global user.email 44811980+SteveRutledge@users.noreply.github.com

    ssh-keygen -t rsa -b 4096 -C 'sterutle@gmail.com'
        copy contents of file ~/.ssh/id_rsa.pub and add under "SSH keys"
        in github -> settings -> ssh and gpg keys

    save passphrase in password manager!

    $ git clone git@github.com:SteveRutledge/python_project_scaffold.git
    cd python_project_scaffold

    #install pyenv
    curl https://pyenv.run | bash

    #install pyenv dependencies
    brew install readline xz

    #what version of python are available?
    pyenv install --list

    #install
    pyenv install 3.8.3
    pyenv install 3.7.7

    #make your fresh pythons available inside the project
    pyenv local 3.8.3 3.7.7

    #install poetry for managing python packing and dependencies
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

    add to ~/.zshrc
        source ~/.poetry/env

    #initialize project
    poetry init --no-interaction
    this will create a .toml file
        tom's obvious, minimal language
        used for a python project config file

    #create managed env for your project, install your package into it, create .lock file
    poetry install
    poetry run python
    the lock file tracks exact versions installed in virtual environment for this project

    #add click package
    poetry install click

    #update to latest  minor update
    poetry update click
    major release changes must be explicit
    poetry add click^7.0

    #run package
    poetry run get_wp
    poetry run get_wp --help
    poetry run get_wp -l de

    #add requests package
    poetry add requests

    #add pytest package, but only as a development dependency
    poetry add --dev pytest

    #run pytest unit tests
    poetry run pytest

    #run pytest with code coverage analysis
    poetry run pytest --cov

    #install nox
    pip install --user --upgrade nox

    configure noxfile.py

    #add mock support to pytest
    poetry add --dev pytest-mock

    #run nox
    nox

    #reuse virtual envs
    nox -r

    #configure nox linting with flake8 using .flake config file
    #lint
    nox -rs lint

    #add blacken to nox
    #blacken
    nox -rs black

    poetry add insecure-package
    nox -rs safety
    poetry remove insecure-package

    #add nox flake8-import-order

    #add nox flake8-bugbear

    #use poetry to maange all dev tools to pin the versions
    poetry add --dev \
    black \
    flake8 \
    flake8-bandit \
    flake8-black \
    flake8-bugbear \
    flake8-import-order \
    safety

    #install pre-commit
    pip install --user --upgrade pre-commit

    #after setting up the .pre-commit-config.yaml, install hooks
    pre-commit install

    #run pre-commit on all files
    pre-commit run --all-files

    #add mypy
    poetry add --dev mypy

    #add nox session to noxfile.py, then run:
       nox -rs mypy

    #overview of dev tasks automated by nox, with docs
    nox --list-sessions

    # add flake8-docstrings plugin to you dev dependences
    poetry add --dev flake8-docstrings

    # add dxdoctest to  dev env
    poetry add --dev xdoctest

    # generate html docs with sphinx
    nox -rs docs
    
