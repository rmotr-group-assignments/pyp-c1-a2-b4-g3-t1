import copy
import unittest
import random

# SORTS
from bubble_sort import bubble_sort

def failing_test(input_list):
    return ["this test will always fail"]

class TestInsertionSort(unittest.TestCase):

    def check_sort(self, pre_sort, post_sort):
        self.assertEqual(bubble_sort(pre_sort), post_sort)

    def test_sort_one_number(self):
        self.check_sort([10], [10])

    def test_sort_multiple_numbers(self):
        self.check_sort([6, 4, 3], [3, 4, 6])
        self.check_sort([20, 50, 10], [10, 20, 50])

    def test_sort_negative_numbers(self):
        self.check_sort([-4, -3, -2], [-4, -3, -2])
        self.check_sort([-4, -100, -20], [-100, -20, -4])

    def test_sort_mix_signs(self):
        self.check_sort([-4, 3, -2, 10], [-4, -2, 3, 10])
        self.check_sort([4, 3, 2, 1, 0, -1, -2, -3, -4],
                        [-4, -3, -2, -1, 0, 1, 2, 3, 4])

    def test_sort_duplicates(self):
        self.check_sort([2, -3, 1, 1, 5, -5], [-5, -3, 1, 1, 2, 5])

    @staticmethod
    def generate_random_ordered_list():
        list_size = random.randint(1000, 2000)
        list_start = random.randint(-500, -250)
        i = list_start
        num_list = []
        for x in range(0, list_size):
            num_list.append(i)
            i += random.randint(0, 100)
        return num_list

    @staticmethod
    def shuffle_list(lst):
        num_list = copy.deepcopy(lst)
        for x in range(0, len(num_list) // 2):
            slot_1 = random.randint(0, len(num_list) - 1)
            slot_2 = random.randint(0, len(num_list) - 1)
            temp = num_list[slot_1]
            num_list[slot_1] = num_list[slot_2]
            num_list[slot_2] = temp
        return num_list

    def test_sort_large_random_set(self):
        sorted_list = TestInsertionSort.generate_random_ordered_list()
        shuffled_list = TestInsertionSort.shuffle_list(sorted_list)
        self.check_sort(shuffled_list, sorted_list)

if __name__ == '__main__':
    unittest.main()