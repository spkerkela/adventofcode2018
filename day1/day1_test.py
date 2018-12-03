import unittest
import day1


class TestDay1(unittest.TestCase):
    def test_frequency(self):
        self.assertEqual(day1.calculate_frequency([1, 1, 1]), 3)
        self.assertEqual(day1.calculate_frequency([1, 1, -2]), 0)
        self.assertEqual(day1.calculate_frequency([-1, -2, -3]), -6)

    def test_repeats(self):
        self.assertEqual(day1.repeats([1, -1]), 0)
        self.assertEqual(day1.repeats([3, 3, 4, -2, -4]), 10)
        self.assertEqual(day1.repeats([-6, 3, 8, 5, -6]), 5)
        self.assertEqual(day1.repeats([7, 7, -2, -7, -4]), 14)


if __name__ == '__main__':
    unittest.main()
