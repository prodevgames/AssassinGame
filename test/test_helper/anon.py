from random import choices
from string import ascii_letters, digits

from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.game import Game


def anon_string(count: int = 10):
    return ''.join(choices(ascii_letters + digits, k=count))


def anon_player():
    return Player(anon_string())


def anon_location():
    return Location(anon_string())


def anon_item():
    return Item(anon_string())


def anon_game(players: set = None, items: set = None, locations: set = None):
    if players is None:
        players = {anon_player(), anon_player(), anon_player()}
    if items is None:
        items = {anon_item(), anon_item(), anon_item()}
    if locations is None:
        locations = {anon_location(), anon_location(), anon_location()}
    game = Game(players, items, locations)
    return game
