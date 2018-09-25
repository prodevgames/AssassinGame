class Location:
    __name: str = None

    def __init__(self, name: str) -> None:
        if not name:
            raise ValueError('name must be at least 1 character')
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError
