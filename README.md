# Zelda-python

Learning to devlope a game in Python with Pygame. Thanks to Clear code.

This codebase is published under the Creative Commons Zero (CC0) license.

## pre-requisites

```sh
brew install pyenv
pip3 install -U pipenv

pyenv install 3.10.4
pyenv global 3.10.4
# or pyenv local 3.10.4
```

```sh
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc

# PATH=$(pyenv root)/shims:$PATH
```

## Project Structure

```tree
.
├── .gitignore
├── .python-version
├── main.py
├── Makefile
├── Pipfile
├── Pipfile.lock
├── README.md
├── setup.cfg
├── assets
    └── audio
    └── graphics
    └── map
├── config
│   ├── __init__.py
│   ├── defaultenv
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
#pyenv install 3.10.4
#pipenv shell
make install

# launch the game 
#python main.py
make run
```
