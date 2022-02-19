import requests

from adafolio.Pool import Pool


ADAFOLIO_PORTFOLIO_URL = "https://adafolio.com/portfolio/download/"


class Portfolio:
    def __init__(self, portfolio):
        self._portfolio_id = portfolio
        self._data = requests.get(ADAFOLIO_PORTFOLIO_URL + portfolio).json()

    @property
    def members(self):
        return [
            Pool(pool["pool_id"].strip(), pool["ticker"].upper().strip())
            for pool in self._data["pools"]
        ]

    def update_members(self, members):
        return {
            "description": self._data["description"],
            "id": self._portfolio_id,
            "name": self._data["name"],
            "pools": [{"id": member.pool_id} for member in members]
        }


def get_members(portfolio):
    """Lists all the members of an adafolio portfolio."""
    return Portfolio(portfolio).members
