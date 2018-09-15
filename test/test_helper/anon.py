from random import choices
from string import ascii_letters, digits

from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player


def anon_string(count: int = 10):
    return ''.join(choices(ascii_letters + digits, k=count))


def anon_player():
    return Player(anon_string())


def anon_location():
    return Location(anon_string())


def anon_item():
    return Item(anon_string())
