class Player:
    __name: str = None

    def __init__(self, name: str) -> None:
        if type(name) is not str:
            raise TypeError("Invalid type given as name to Player")
        if len(name) <= 0:
            raise ValueError("Name cannot be an empty string for Player")
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False

        return self.__name == other.__name

    def __hash__(self):
        count = 0
        for character in self.__name:
            count += ord(character)
        return count
