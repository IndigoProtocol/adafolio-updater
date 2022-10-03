from typing import List

import requests

from adafolio.member import Member

CSPA_MEMBER_LIST = (
    "https://raw.githubusercontent.com/"
    + "SinglePoolAlliance/Registration/master/registry.json"
)


def get_members() -> List[Member]:
    """Gets a list of all the members in the CSPA."""
    return [
        Member(member["poolId"], member["ticker"])
        for member in requests.get(CSPA_MEMBER_LIST).json()
    ]
