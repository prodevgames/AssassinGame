class Player:
    __name: str = None

    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self):
        raise NotImplementedError
