def bubble_sort(lst):
    for i in xrange(len(lst)-1, 0, -1):
        oper_list = lst[:i+1]
        for j in xrange(0, len(oper_list)-1):
            if lst[j] > lst[j+1]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst