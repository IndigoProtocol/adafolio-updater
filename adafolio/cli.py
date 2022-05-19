import json
import os
import sys

import click
import requests

from adafolio.member import Member
import adafolio.cspa
import adafolio.portfolio


ASPA = "10e9fb44-a712-11ec-b375-0242ac190002"
HIGH_PERFORMERS = "84a2d806-fe0f-11ea-befd-a45e60be653b"


@click.group()
def folio():
    """A simple interface for managing adafolio lists."""
    pass


def _print_member(member, show_ticker):
    if show_ticker:
        print(member.ticker)

    else:
        print(member.member_id)


@folio.command()
@click.argument("portfolio")
@click.option("--tickers", "-t", is_flag=True, help="Show only tickers")
def members(portfolio, tickers):
    """Lists all the members of an adafolio portfolio."""
    for member in adafolio.portfolio.get_members(portfolio):
        _print_member(member, tickers)


@folio.command()
@click.option("--tickers", "-t", is_flag=True, help="Show only tickers")
def cspa(tickers):
    """Lists all the members in the CSPA."""
    for member in adafolio.cspa.get_members():
        _print_member(member, tickers)


@folio.command()
@click.option("--tickers", "-t", is_flag=True, help="Show only tickers")
def aspa(tickers):
    """Lists all the members in the ASPA."""
    for member in adafolio.portfolio.get_members(ASPA):
        _print_member(member, tickers)


@folio.command()
@click.option("--tickers", "-t", is_flag=True, help="Show only tickers")
def cspa_aspa(tickers):
    """Lists all the members in both the CSPA and ASPA."""
    aspa_members = adafolio.portfolio.get_members(ASPA)
    for member in adafolio.cspa.get_members():
        if member in aspa_members:
            _print_member(member, tickers)


@folio.command()
@click.option("--tickers", "-t", is_flag=True, help="Show only tickers")
def high_performance_cspa(tickers):
    """Lists all the members in the CSPA that are high performers."""
    high_performance_members = adafolio.portfolio.get_members(HIGH_PERFORMERS)
    for member in adafolio.cspa.get_members():
        if member in high_performance_members:
            _print_member(member, tickers)


@folio.command()
@click.argument("portfolio")
@click.option("--api-key", help="Your adafolio API key")
@click.argument("members", type=click.File("r"), default=sys.stdin)
def update(portfolio, api_key, members):
    """Updates a portfolio with a list of members.
    """
    with members as m:
        members = m.read().splitlines()

    members = [Member(member) for member in members]

    if not api_key:
        try:
            api_key = os.environ["ADAFOLIO_API_KEY"]

        except KeyError:
            raise click.UsageError("adafolio API key must be provided")

    portfolio = adafolio.portfolio.Portfolio(portfolio)
    portfolio.update_members(members)

    print(json.dumps(requests.post(
        "https://api.adafolio.com/create-portfolio",
        json=portfolio.json,
        headers={"API-KEY": api_key}
    ).json(), indent=4))
