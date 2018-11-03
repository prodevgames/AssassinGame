from assassin_game_csss.domain.upid import UPID
from typing import Union


class Player:
    __name: str = None
    __upid: UPID = None

    def __init__(self, name: str, upid: Union[UPID, str]) -> None:
        if type(name) is not str:
            raise TypeError("Invalid type given as name to Player")
        if len(name) <= 0:
            raise ValueError("Name cannot be an empty string for Player")
        self.__name = name

        if type(upid) is str:
            upid = UPID(upid)
        if type(upid) is not UPID:
            raise TypeError("upid must be UPID or str")
        self.__upid = upid

    @property
    def name(self) -> str:
        return self.__name

    @property
    def upid(self) -> UPID:
        return self.__upid

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False

        return self.__upid == other.__upid

    def __hash__(self):
        return hash(self.__upid)

    def __str__(self):
        return self.__name

    def __repr__(self):
        return "%s(\"%s\",%s)" % (self.__class__.__name__, self.__name, repr(self.__upid))
