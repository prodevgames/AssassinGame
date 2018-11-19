import json

from assassin_game_csss.adapter.dto.item_dto import ItemDto
from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.repository.abstract_item_repo import AbstractItemRepo


class JsonItemRepo(AbstractItemRepo):

    __file_path: str = None

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def save(self, item: Item) -> None:
        if type(item) is not Item:
            raise TypeError("Invalid type given as item argument")

        items = self.__retrieve_from_json()
        items.add(item)
        self.__save_to_json(items)

    def retrieve_all(self) -> set:
        return self.__retrieve_from_json()

    def delete(self, item: Item) -> None:
        if type(item) is not Item:
            raise TypeError("Invalid type given as item argument")

        items = self.__retrieve_from_json()
        items.remove(item)
        self.__save_to_json(items)

    def __retrieve_from_json(self) -> set:
        with open(self.__file_path, "r") as file:
            return set([ItemDto.to_domain(item_data) for item_data in json.load(file)])

    def __save_to_json(self, items: set) -> None:
        with open(self.__file_path, "w") as file:
            json.dump([ItemDto(item) for item in items], file)
