from uuid import UUID

from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.target import Target


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

    def get_score(self, player) -> int:
        raise NotImplementedError

    def get_target(self, player: Player) -> Target:
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def end(self):
        raise NotImplementedError

    def confirm_kill(self, player: Player, target: Target) -> bool:
        raise NotImplementedError

    def get_game_id(self):
        raise NotImplementedError
