import click
import requests

import adafolio.cspa


@click.group()
def folio():
    """A simple interface for managing adafolio lists."""
    pass


@folio.command()
@click.argument("portfolio")
def members(portfolio):
    """Lists all the members of an adafolio portfolio."""
    r = requests.get("https://adafolio.com/portfolio/download/" + portfolio)

    for pool in r.json()["pools"]:
        print(pool["ticker"])


@folio.command()
def cspa():
    """Lists all the members in the CSPA."""
    for member in adafolio.cspa.get_members():
        print(member)
