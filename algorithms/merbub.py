# **Sorting** - Implement two types of sorting algorithms: Merge sort and bubble sort.

from random import randint

def bubble_sort(unsorted: list):
    '''
    Sort input list lowest-to-highest using bubble sort algorithm.
    '''
    switch_occurred = False
    while not switch_occurred:
        for index, value in enumerate(unsorted):
            try:
                if value > unsorted[index + 1]:
                    unsorted[index], unsorted[index + 1] = unsorted[index + 1], unsorted[index]
                    switch_occurred = True
            except IndexError:
                break
        
        if not switch_occurred:
            sorted_list = unsorted
            return sorted_list
        else:
            switch_occurred = False

def merge_sort(unsorted_list: list):
    '''
    Sort input list from highest-to-lowest using merge sort algorithm.
    '''
    assert type(unsorted_list) == list, f'parameter {unsorted_list} must be a list.'

    def merge(a, b):
        merged_list = []
        while a and b:
            if a[0] < b[0]:
                merged_list.append(b.pop(0))
            else:
                merged_list.append(a.pop(0))

        merged_list.extend(a)
        merged_list.extend(b)
        return merged_list

    if len(unsorted_list) <= 1:
        return unsorted_list

    midpoint = len(unsorted_list) // 2
    left, right = unsorted_list[:midpoint], unsorted_list[midpoint:]
    left = merge_sort(left)
    right = merge_sort(right)
    sorted_list = merge(left, right)

    return sorted_list


def random_list(nel):
    '''
    Generate a list of random integers (0-99) that has `nel` number of
    elements.
    '''
    output = []
    for i in range(nel):
        output.append(randint(0,99))
    return output

rlist = random_list(12)

print(bubble_sort(rlist))
print(merge_sort(rlist))