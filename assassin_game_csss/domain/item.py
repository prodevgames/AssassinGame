class Item:
    __name: str = None

    def __init__(self, name: str) -> None:
        if type(name) is not str:
            raise TypeError("Argument 'name' must be an instance of 'str'")
        if len(name) == 0:
            raise ValueError('name must be at least 1 character')
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError
