class Item:
    __name: str = None

    def __init__(self, name: str) -> None:
        if type(name) is not str:
            raise TypeError("Argument name must be of type str")
        if len(name) == 0:
            raise ValueError("Argument name must be at least 1 character")
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False

        return self.__name == other.__name

    def __hash__(self):
        return hash(self.__name)
