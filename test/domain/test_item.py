from unittest import TestCase, skip

from assassin_game_csss.domain.item import Item


# noinspection PyTypeChecker
class TestItem(TestCase):
    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedNone(self):
        # Act
        def action(): Item(None)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedInt(self):
        # Act
        def action(): Item(3)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedFloat(self):
        # Act
        def action(): Item(3.4)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedDict(self):
        # Act
        def action(): Item(3)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedList(self):
        # Act
        def action(): Item(3)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
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
