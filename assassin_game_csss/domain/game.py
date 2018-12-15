from uuid import UUID

from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.target import Target
from assassin_game_csss.domain.game_state import GameState


class Game:
    __name: str = None
    __id: UUID = None
    __players: set = None
    __scores: dict = None
    __targets: dict = None

    def __init__(self, players: set, items: set, locations: set, num_targets: int = 1) -> None:
        raise NotImplementedError

    @property
    def id(self) -> UUID:
        raise NotImplementedError

    @property
    def status(self) -> GameState:
        raise NotImplementedError

    def get_score(self, player) -> int:
        raise NotImplementedError

    def get_target(self, player: Player) -> Target:
        raise NotImplementedError

    def start(self) -> None:
        raise NotImplementedError

    def end(self) -> None:
        raise NotImplementedError

    def mark_kill(self, player: Player, target: Target) -> bool:
        raise NotImplementedError
