import requests

from adafolio.Pool import Pool


ADAFOLIO_PORTFOLIO_URL = "https://adafolio.com/portfolio/download/"


class Portfolio:
    def __init__(self, portfolio):
        self._data = requests.get(ADAFOLIO_PORTFOLIO_URL + portfolio).json()

    def get_members(self):
        return [
            Pool(pool["pool_id"].strip(), pool["ticker"].upper().strip())
            for pool in self._data["pools"]
        ]


def get_members(portfolio):
    """Lists all the members of an adafolio portfolio."""
    return Portfolio(portfolio).get_members()
