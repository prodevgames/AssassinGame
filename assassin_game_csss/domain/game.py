from typing import Set, Dict
from uuid import UUID
from random import randint

from assassin_game_csss.domain.game_state import GameState
from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.target import Target


class Game:
    __name: str = None
    __id: UUID = None
    __players: Set[Player] = None
    __scores: dict = None
    __targets: Dict[Player, Target] = None

    def __init__(self, players: Set[Player], items: Set[Item], locations: Set[Location], num_targets: int = 1) -> None:
        # Type Checking
        if not isinstance(players, set) or any(not isinstance(player, Player) for player in players):
            raise TypeError("The 'players' argument must be a set of Player objects")
        elif not isinstance(items, set) or any(not isinstance(item, Item) for item in items):
            raise TypeError("The 'items' argument must be a set of Item objects")
        elif not isinstance(locations, set) or any(not isinstance(location, Location) for location in locations):
            raise TypeError("The 'locations' argument must be a set of Location objects")

        if len(players) < 2:
            raise ValueError("A game cannot be constructed with fewer than 2 players")
        elif len(items) < 1:
            raise ValueError("A game cannot be constructed with fewer than 1 items")
        elif len(locations) < 1:
            raise ValueError("A game cannot be constructed with fewer than 1 locations")

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
