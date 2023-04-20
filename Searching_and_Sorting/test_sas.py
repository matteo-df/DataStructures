import unittest
from binary_search import binary_search


class SearchSortTestCase(unittest.TestCase):
    def test_binary_search(self):
        odd_length_list = [3, 7, 9, 14, 19, 24, 27]
        even_length_list = [3, 7, 9, 14, 19, 24]

        # search values not present in the lists
        self.assertEqual(binary_search(odd_length_list, 0), -1)
        self.assertEqual(binary_search(even_length_list, 0), -1)
        self.assertEqual(binary_search(odd_length_list, 100), -1)
        self.assertEqual(binary_search(even_length_list, 100), -1)

        # search each value of the lists
        for idx, value in enumerate(odd_length_list):
            self.assertEqual(binary_search(odd_length_list, value), idx)
        for idx, value in enumerate(even_length_list):
            self.assertEqual(binary_search(even_length_list, value), idx)


if __name__ == '__main__':
    unittest.main()
