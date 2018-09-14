class Player:
    __name: str = None

    def __init__(self, name: str) -> None:
        __name = name

    def get_name(self):
        return self.__name
