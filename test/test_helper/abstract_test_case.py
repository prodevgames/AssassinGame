from unittest import TestCase


class AbstractTestCase(TestCase):

    def _get_instance(self):
        self.skipTest("Abstract")
