import json
import os
import sys

import click
import requests

import adafolio.cspa
import adafolio.portfolio


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
def high_performance_cspa(tickers):
    """Lists all the members in the CSPA that are high performers."""
    high_performance_members = adafolio.portfolio.get_members(HIGH_PERFORMERS)
    for member in adafolio.cspa.get_members():
        if member in high_performance_members:
            _print_member(member, tickers)


@folio.command()
@click.argument("portfolio")
@click.option("--api-key", help="Your adafolio API key")
def update_cspa(portfolio, api_key):
    """Prints out JSON required to update members to all members of the
    CSPA. If API key is provided then submits the request automatically."""
    p = adafolio.portfolio.Portfolio(portfolio)
    updated_portfolio = p.update_members(adafolio.cspa.get_members())

    if api_key:
        updated_portfolio = requests.post(
            "https://api.adafolio.com/create-portfolio",
            json=updated_portfolio,
            headers={"API-KEY": api_key}
        ).json()

    print(json.dumps(updated_portfolio,indent=4))
