import re

MEMBER_ID_LENGTH = 56


class Member:
    def __init__(self, member_id: str, ticker: str = "") -> None:
        if not member_id or not member_id.strip():
            raise ValueError("member_id must be set")

        member_id = member_id.strip()
        if len(member_id) != MEMBER_ID_LENGTH:
            raise ValueError("member_id is invalid", member_id)

        self._member_id = member_id

        self._ticker = ""
        if ticker:
            match = re.match(r"[\w]+", ticker.upper())
            if not match:
                raise ValueError("ticker is invalid", ticker)

            self._ticker = match.group()

    @property
    def member_id(self) -> str:
        return self._member_id

    @property
    def ticker(self) -> str:
        return self._ticker

    def __str__(self) -> str:
        if self.ticker:
            return self.ticker

        return self.member_id

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        if type(other) == Member:
            return self.member_id == other.member_id

        return False
