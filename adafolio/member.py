import re


class Member:
    def __init__(self, member_id, ticker):
        if not member_id or not member_id.strip():
            raise ValueError("member_id must be set")

        self._member_id = member_id.strip()

        self._ticker = ""
        if ticker:
            self._ticker = re.match(r"[\w]+", ticker.upper()).group()

    @property
    def member_id(self):
        return self._member_id

    @property
    def ticker(self):
        return self._ticker

    def __str__(self):
        if self.ticker:
            return self.ticker

        return self.member_id

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if type(other) == type(self):
            return self.member_id == other.member_id

        return False
