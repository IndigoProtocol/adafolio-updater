import requests


CSPA_MEMBER_LIST = "https://raw.githubusercontent.com/SinglePoolAlliance/Registration/master/registry.json"


def get_members():
    """Gets a list of all the members in the CSPA."""
    return [
        member["ticker"].strip().upper()
        for member in requests.get(CSPA_MEMBER_LIST).json()
    ]
