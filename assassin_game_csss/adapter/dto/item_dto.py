from assassin_game_csss.domain.item import Item


class ItemDto(dict):

    def __init__(self, item: Item, **kwargs):
        super().__init__(**kwargs)
        self["name"] = item.name

    @staticmethod
    def to_domain(item_dto):
        return Item(item_dto["name"])
