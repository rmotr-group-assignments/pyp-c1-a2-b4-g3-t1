"""Implementation of insertion sort algorithm in python

Starting at the beginning of the list find the appropriate position for each
element and reposition it
Space complexity:
n is the size of the list
O(n^3) - creates a new list of size n, n^2 times; not implicit in the algorithm
just this implementation

Time Complexity:
n is the size of the list
O(n^2)"""


def insertion_sort(num_list):
    num_list = ["_"] + num_list
    for i in range(2, len(num_list)):
        insert_val = num_list[i]
        for j in range(1, i):
            if num_list[j] > insert_val:
                num_list = num_list[:j] + [insert_val] + (num_list[j:i] +
                                                          num_list[i+1:])
                break
    return num_list[1:]
