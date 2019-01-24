from os import remove, close
from tempfile import mkstemp

from assassin_game_csss.adapter.repository.json_item_repo import JsonItemRepo
from test.domain.repository.test_abstract_item_repo import TestAbstractItemRepo


class TestJsonItemRepo(TestAbstractItemRepo):
    __json_item_repo_file_path = None

    def setUp(self):
        file_descriptor, file_path = mkstemp(prefix="assassinGameTempTestFile_")
        self.__json_item_repo_file_path = file_path
        with open(self.__json_item_repo_file_path, "w") as file:
            file.write("[]")
        close(file_descriptor)
        super().setUp()

    def tearDown(self):
        remove(self.__json_item_repo_file_path)
        super().tearDown()

    def _get_instance(self):
        return JsonItemRepo(self.__json_item_repo_file_path)
