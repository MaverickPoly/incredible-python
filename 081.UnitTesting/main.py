import unittest


def bubble_sort(lst: list[int]):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def calc_square(x: int):
    return x ** 2



class BubbleSortTest(unittest.TestCase):
    def test_simple_lists(self):
        l1 = [4, 2, 5, 1, 8, 6, 9]
        l_copy = l1[:]
        bubble_sort(l_copy)
        self.assertEqual(l_copy, sorted(l1))


def test_assertions():
    assert calc_square(2) == 4
    assert calc_square(5) == 25


if __name__ == '__main__':
    unittest.main()
    test_assertions()
