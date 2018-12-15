from typing import Set
from uuid import UUID

from assassin_game_csss.domain.game_state import GameState
from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.target import Target


class Game:
    __name: str = None
    __id: UUID = None
    __players: set = None
    __scores: dict = None
    __targets: dict = None

    def __init__(self, players: Set[Player], items: Set[Item], locations: Set[Location], num_targets: int = 1) -> None:
        # Type Checking

        # Game Initialization Logic
        raise NotImplementedError

    @property
    def id(self) -> UUID:
        return self.__id

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
