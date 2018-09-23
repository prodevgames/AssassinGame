class Player:
    __name: str = None

    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError
