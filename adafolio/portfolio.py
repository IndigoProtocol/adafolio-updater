import requests

from adafolio.Pool import Pool


ADAFOLIO_PORTFOLIO_URL = "https://adafolio.com/portfolio/download/"


def get_members(portfolio):
    """Lists all the members of an adafolio portfolio."""
    return [
        Pool(pool["pool_id"].strip(), pool["ticker"].upper().strip())
        for pool in requests.get(
            ADAFOLIO_PORTFOLIO_URL + portfolio).json()["pools"]
    ]
