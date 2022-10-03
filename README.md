Adafolio Updater
================

A tool for managing an [adafolio](https://adafolio.com/) list.

This tool is primarily created for automatically syncing the [CSPA list
on
adafolio](https://adafolio.com/portfolio/e7f0b9c0-9bd8-11eb-b77a-0242ac1d0002).
However, it can be adapted to work with any adafolio list.

Installation
------------

The adafolio-updater (`folio`) tool is a CLI app written in Python3.
It's installable via pip. It's recommended to install inside a virtual
environment. Create a virtual environment using venv:

    python3 -m venv venv

Activate the virtual environment. In Linux:

    source venv/bin/activate

In Windows:

    .\venv\Scripts\activate

After the virtual environment is activated, install the pip:

    pip install -e .

Alternatively, a Docker container is provided:

    docker build -t adafolio-updater .
    docker run adafolio-updater folio --help

Usage
-----

After installation, the tool will be available via the `folio` command.
Running the `--help` option will show all the available commands for the
tool.

    $ folio --help
    Usage: folio [OPTIONS] COMMAND [ARGS]...

      A simple interface for managing adafolio lists.

    Options:
      --help  Show this message and exit.

    Commands:
      aspa                   Lists all the members in the ASPA.
      cspa                   Lists all the members in the CSPA.
      cspa-aspa              Lists all the members in both the CSPA and ASPA.
      high-performance-cspa  Lists all the members in the CSPA that are high...
      members                Lists all the members of an adafolio portfolio.
      update                 Updates a portfolio with a list of members.

`folio cspa` gets a list of all pools [registered in the
CSPA](https://github.com/SinglePoolAlliance/Registration).

`folio update` updates a particular list on adafolio. To update a list,
an [adafolio API](https://api.adafolio.com/ui/) key must be provided
that has permission to update.

The pools can be piped into `folio update`, for example:

    folio cspa | folio update [API-KEY]

Development
-----------

This project makes use of Python tools to enforce coding standards and
validate accuracy. To install the Python development tools, run:

    pip install -r requirements-dev.txt

This project also makes use of git pre-commit hooks. To set up the
hooks, ensure you have `git` and `pre-commit` installed then run:

    pre-commit install

You can verify if the git hook is working properly by running:

    pre-commit run --all-files

Before code is committed to this repository it must pass automated
checks for code conformity. The git hook will automatically refactor
code to ensure compliance.
