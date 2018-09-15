from uuid import UUID


class Game:
    __name: str = None
    __id: UUID = None
    __players: set = None
    __scores: dict = None
    __targets: dict = None

    def __init__(self, players: set, items: set, locations: set, num_targets: int = 1):
        raise NotImplementedError

    def get_status(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def end(self):
        raise NotImplementedError

