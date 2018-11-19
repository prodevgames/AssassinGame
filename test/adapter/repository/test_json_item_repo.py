from assassin_game_csss.adapter.repository.json_item_repo import JsonItemRepo
from test.domain.repository.test_abstract_item_repo import TestAbstractItemRepo


class TestInMemoryItemRepo(TestAbstractItemRepo):

    def _get_instance(self):
        return JsonItemRepo("savedItems.json")
