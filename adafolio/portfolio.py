import requests


ADAFOLIO_PORTFOLIO_URL = "https://adafolio.com/portfolio/download/"


def get_members(portfolio):
    """Lists all the members of an adafolio portfolio."""
    return [
        pool["ticker"].strip().upper() for pool in requests.get(
            ADAFOLIO_PORTFOLIO_URL + portfolio).json()["pools"]
    ]
