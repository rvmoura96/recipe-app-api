from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers_should_return_4_when_x_2_and_y_2(self):
        self.assertEqual(add(2, 2), 4)

    def test_add_numbers_should_return_800_when_x_650_and_y_150(self):
        self.assertEqual(add(650, 150), 800)

    def test_subtract_numbers_should_2_when_x_101_and_y_99(self):
        self.assertEqual(subtract(101, 99), 2)
