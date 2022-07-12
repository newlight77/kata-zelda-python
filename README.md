# Zelda-python

Learning to devlope a game in Python with Pygame. Thanks to Clear code.

This codebase is published under the Creative Commons Zero (CC0) license.

## pre-requisites

```sh
brew install pyenv
pip3 install -U pipenv

pyenv install 3.10.4
pyenv global 3.10.4

pyenv local 3.10.4
```

### Mac OSX

```sh
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc

# PATH=$(pyenv root)/shims:$PATH
```

## Setup project

```sh
# To find the location of the virtual environment
pipenv --venv

# check which dependencies are mismatched
pipenv check

# see which sub-dependencies are installed by packages
pipenv graph --reverse

# installing new dependencies
pipenv install python-dotenv colorlog gunicorn
pipenv install email-listener 

# install dev dependencies for use during development
pipenv install --dev yapf
```

## Project Structure

```tree
.
├── .gitignore
├── .python-version
├── Makefile
├── main.py
├── makefile
├── Pipfile
├── Pipfile.lock
├── README.md
├── setup.cfg
├── config
│   ├── __init__.py
│   ├── default.py
│   ├── gunicorn.py
│   └── logger.py
│   └── pygame.py
├── src
│   ├── debug.py
│   ├── game.py
│   ├── level.py
│   ├── player.py
│   ├── settings.py
│   ├── tile.py
└── tools
    └── linter
        ├── __init__.py
        ├── lint.sh
        ├── run-mccabe.py
        ├── run-pyflakes.py
        └── utils.py
```

## Run

```sh
# set up Pipenv in your project
pipenv install

# activate the virtual environment
pipenv shell

# launch the game 
ENV=ci gunicorn --reload --config config/gunicorn.conf.py main:run
```

## Deploy

```sh
# Deploying
pipenv install --deploy
```