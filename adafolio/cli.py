import click

import adafolio.cspa


@click.group()
def folio():
    """A simple interface for managing adafolio lists."""
    pass


@folio.command()
def cspa():
    """Lists all the members in the CSPA."""
    for member in adafolio.cspa.get_members():
        print(member)
