class Location:
    __name: str = None

    def __init__(self, name: str) -> None:
        if type(name) != str:
            raise TypeError('name of Location must be a string')
        elif len(name) <= 0:
            raise ValueError("name of Location must be non-empty")
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        return self.__name == other.__name

    def __hash__(self):
        return hash(self.__name)
