# Adafolio Updater

A tool for managing an [adafolio](https://adafolio.com/) list.

## Usage

### Docker

    docker build -t adafolio-updater .
    docker run adafolio-updater folio --help

### Virtualenv

	virtualenv venv
	pip install -e .
	venv/bin/folio --help
