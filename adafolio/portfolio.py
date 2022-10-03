from typing import Any, Dict, List

import requests

from adafolio.member import Member

ADAFOLIO_PORTFOLIO_URL = "https://adafolio.com/portfolio/download/"


class Portfolio:
    def __init__(self, portfolio: str) -> None:
        self._portfolio_id = portfolio
        self._data = requests.get(ADAFOLIO_PORTFOLIO_URL + portfolio).json()
        self._members = [
            Member(pool["pool_id"], pool["ticker"])
            for pool in self._data["pools"]
        ]

    @property
    def members(self) -> List[Member]:
        return self._members

    @property
    def json(self) -> Dict[str, Any]:
        return {
            "description": self._data["description"],
            "id": self._portfolio_id,
            "name": self._data["name"],
            "pools": [{"id": member.member_id} for member in self._members],
        }

    def update_members(self, members: List[Member]) -> None:
        for member in members:
            if not type(member) == Member:
                raise ValueError("members must be a list of Member instances")

        self._members = members


def get_members(portfolio: str) -> List[Member]:
    """Lists all the members of an adafolio portfolio."""
    return Portfolio(portfolio).members
