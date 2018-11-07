import random
from itertools import count
from functools import wraps
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


def counter(func):
    index = count(random.randint(0, 1<<63))

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(next(index), *args, **kwargs)

    return wrapper

def trim_char(index, chars):
    new_index, char = divmod(index, len(chars))
    return new_index, chars[char]

@counter
def anon_string(index, length: int = 10):
    chars = digits + ascii_letters
    to_join = []
    for _ in range(length):
        index, c = trim_char(index, chars)
        to_join.append(c)
    return ''.join(to_join)


@counter
def anon_upid(index):
    to_join = []

    for _ in range(3):
        index, c = trim_char(index, ascii_lowercase)
        to_join.append(c)

    for _ in range(3):
        index, c = trim_char(index, digits)
        to_join.append(c)

    return UPID(''.join(to_join))


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
