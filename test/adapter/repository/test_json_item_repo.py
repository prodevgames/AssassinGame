from os import remove

from assassin_game_csss.adapter.repository.json_item_repo import JsonItemRepo
from test.domain.repository.test_abstract_item_repo import TestAbstractItemRepo


class TestInMemoryItemRepo(TestAbstractItemRepo):
    __json_item_repo_file = "savedItems.json"

    def setUp(self):
        with open(self.__json_item_repo_file, "w+") as file:
            file.write("[]")
        super().setUp()

    def tearDown(self):
        remove(self.__json_item_repo_file)
        super().tearDown()

    def _get_instance(self):
        return JsonItemRepo(self.__json_item_repo_file)
