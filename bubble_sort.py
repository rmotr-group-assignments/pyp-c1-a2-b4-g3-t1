def bubble_sort(lst):
    for i in xrange(len(lst)-1, 0, -1):
        for j in xrange(i):
            if lst[j] > lst[j+1]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst