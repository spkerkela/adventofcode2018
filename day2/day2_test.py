import unittest
import day2


class TestDay2(unittest.TestCase):
    def test_process_ids(self):
        ids = [
            'abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab'
        ]
        self.assertEqual(day2.process_ids(ids), 12)

    def test_contains_n(self):
        self.assertFalse(day2.contains_n('abcdef', 2))
        self.assertTrue(day2.contains_n('bababc', 2))
        self.assertTrue(day2.contains_n('bababc', 3))

        self.assertTrue(day2.contains_n('abbcde', 2))
        self.assertFalse(day2.contains_n('abbcde', 3))
        self.assertFalse(day2.contains_n('abcccd', 2))
        self.assertTrue(day2.contains_n('abcccd', 3))

        self.assertTrue(day2.contains_n('aa', 2))
        self.assertTrue(day2.contains_n('aaa', 3))
        self.assertFalse(day2.contains_n('aaba', 4))
        self.assertFalse(day2.contains_n('ab', 2))
        self.assertFalse(day2.contains_n('abb', 3))


if __name__ == '__main__':
    unittest.main()
