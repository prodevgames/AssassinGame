from assassin_game_csss.domain.upid import UPID

class Player:
    __name: str = None
    __upid: UPID = None

    def __init__(self, name: str, upid: UPID) -> None:
        if type(name) is not str:
            raise TypeError("Invalid type given as name to Player")
        if len(name) <= 0:
            raise ValueError("Name cannot be an empty string for Player")
        if type(upid) is not UPID and type(upid) is not str:
            raise TypeError("Invalid type given to Player UPID")
        if type(upid) is str:
            if len(upid) <= 0:
                raise ValueError()
            else:
                self.__upid = UPID(upid)
        else:
            self.__upid = upid

        self.__name = name

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
