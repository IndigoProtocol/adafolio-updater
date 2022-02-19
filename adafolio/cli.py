import click
import requests

import adafolio.cspa
import adafolio.portfolio


@click.group()
def folio():
    """A simple interface for managing adafolio lists."""
    pass


@folio.command()
@click.argument("portfolio")
def members(portfolio):
    """Lists all the members of an adafolio portfolio."""
    for member in adafolio.portfolio.get_members(portfolio):
        print(member.ticker)


@folio.command()
@click.argument("portfolio")
def diff(portfolio):
    """Lists all the differences between the given adafolio portfolio and the
    CSPA members."""
    cspa_members = adafolio.cspa.get_members()
    adafolio_members = adafolio.portfolio.get_members(portfolio)

    print("To remove:")

    for member in adafolio_members:
        if member.pool_id not in (m.pool_id for m in cspa_members):
            print(member.ticker)

    print()
    print("To add:")

    for member in cspa_members:
        if member.pool_id not in (m.pool_id for m in adafolio_members):
            print(member.ticker)


@folio.command()
def cspa():
    """Lists all the members in the CSPA."""
    for member in adafolio.cspa.get_members():
        print(member.ticker)
