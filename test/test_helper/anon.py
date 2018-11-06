from functools import wraps
from itertools import product
from string import (
    ascii_letters,
    ascii_lowercase,
    digits,
)

from assassin_game_csss.domain.game import Game
from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.target import Target
from assassin_game_csss.domain.upid import UPID


def anon_product(*args, **kwargs):
    def decorator(func):
        def iterator():
            while ...:
                yield from product(*args, **kwargs)
        iterator = iterator()

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(next(iterator), *args, **kwargs)

        return wrapper
    return decorator


@anon_product(ascii_letters + digits, repeat=10)
def anon_string(prod, count: int = 10):
    # TODO: strings of specific length
    return ''.join(prod)


@anon_product(*(ascii_lowercase,)*3, *(digits,)*3)
def anon_upid(prod):
    return UPID(''.join(prod))


def anon_player() -> Player:
    return Player(anon_string(), anon_upid())


def anon_location() -> Location:
    return Location(anon_string())


def anon_item() -> Item:
    return Item(anon_string())


def anon_target() -> Target:
    return Target(anon_player(), anon_item(), anon_location())


def anon_game(players: set = None, items: set = None, locations: set = None) -> Game:
    if players is None:
        players = {anon_player(), anon_player(), anon_player()}
    if items is None:
        items = {anon_item(), anon_item(), anon_item()}
    if locations is None:
        locations = {anon_location(), anon_location(), anon_location()}
    game = Game(players, items, locations)
    return game
