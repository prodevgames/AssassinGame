from re import compile


class UPID:
    __upid: str = None
    __upid_pattern = compile("^[a-z]{3}[0-9]{3}$")

    def __init__(self, upid: str) -> None:

        if type(upid) is not str:
            raise TypeError("Provided upid arg must be a string")

        upid = upid.lower()

        if not self.__upid_pattern.match(upid):
            raise ValueError("Provided upid arg must match 'abc123' pattern")

        self.__upid = upid

    @property
    def upid(self) -> str:
        return self.__upid

    def __eq__(self, other):
        if not isinstance(other, UPID):
            return False

        return self.__upid == other.__upid

    def __hash__(self):
        return hash(self.__upid)
