from random import sample, shuffle
from typing import Set, Dict
from uuid import UUID, uuid4

from assassin_game_csss.domain.game_state import GameState
from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.target import Target


class Game:
    __name: str = None
    __id: UUID = None
    __status: GameState = None
    __players: Set[Player] = None
    __scores: Dict[Player, int] = None
    __targets: Dict[Player, Target] = None

    def __init__(self, players: Set[Player], items: Set[Item], locations: Set[Location], num_targets: int = 1) -> None:
        # Type Checking
        if not isinstance(players, set) or any(not isinstance(player, Player) for player in players):
            raise TypeError("The 'players' argument must be a set of Player objects")
        elif not isinstance(items, set) or any(not isinstance(item, Item) for item in items):
            raise TypeError("The 'items' argument must be a set of Item objects")
        elif not isinstance(locations, set) or any(not isinstance(location, Location) for location in locations):
            raise TypeError("The 'locations' argument must be a set of Location objects")
        elif not isinstance(num_targets, int):
            raise TypeError("The 'num_targets' argument must be an int")

        if len(players) < 2:
            raise ValueError("A game cannot be constructed with fewer than 2 players")
        elif len(items) < 1:
            raise ValueError("A game cannot be constructed with fewer than 1 items")
        elif len(locations) < 1:
            raise ValueError("A game cannot be constructed with fewer than 1 locations")
        elif num_targets < 1:
            raise ValueError("A game cannot be constructed with fewer than 1 target per player")

        # TODO GH 2018-Sep-15: Add functionality to support multiple targets and remove this when done
        if num_targets != 1:
            raise NotImplementedError("The multiple-target game feature is not yet supported")

        # Game Initialization Logic
        self.__status = GameState.CREATED
        self.__id = uuid4()
        self.__scores = dict()
        self.__targets = dict()
        self.__players = players
        players = list(players)
        shuffle(players)
        for index, player in enumerate(players):
            self.__scores[player] = 0
            self.__targets[player] = Target(players[(index + 1) % len(players)],
                                            sample(items, 1)[0],
                                            sample(locations, 1)[0])

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def status(self) -> GameState:
        return self.__status

    def get_score(self, player: Player) -> int:
        if not isinstance(player, Player):
            raise TypeError("Cannot get the score of a non-player argument")
        elif player not in self.__players:
            raise ValueError("Player '%s' not found in game" % player)
        return self.__scores[player]

    def get_target(self, player: Player) -> Target:
        if not isinstance(player, Player):
            raise TypeError("Cannot get the target of a non-player argument")
        elif player not in self.__players:
            raise ValueError("Player '%s' not found in game" % player)
        return self.__targets[player]

    def start(self) -> None:
        if self.__status is not GameState.CREATED:
            raise RuntimeError("Invalid state, cannot start game from state '%s'" % self.__status)
        self.__status = GameState.STARTED

    def end(self) -> None:
        if self.__status is not GameState.STARTED:
            raise RuntimeError("Invalid state, cannot end game from state '%s'" % self.__status)
        self.__status = GameState.ENDED

    def mark_kill(self, player: Player, target: Target) -> bool:
        raise NotImplementedError
