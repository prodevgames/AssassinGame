from unittest import TestCase, skip

from assassin_game_csss.domain.item import Item


class TestItem(TestCase):
    def test__constructor__shouldThrowException__whenProvidedNone(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Item(None)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedInt(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Item(3)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedFloat(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Item(3.4)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedDict(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Item(3)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedList(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Item(3)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedEmptyString(self):
        # Act
        def action(): Item("")

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__get_name__shouldReturnName(self):
        expected_name = "Test Name"
        item = Item(expected_name)
        self.assertEqual(expected_name, item.get_name())

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnTrue__whenConstructionIsIdentical(self):
        # Arrange
        item_a = Item("Identical Name")
        item_b = Item("Identical Name")

        # Act
        actual = (item_a == item_b)

        # Assert
        self.assertTrue(actual)
