# **Sorting** - Implement two types of sorting algorithms: Merge sort and bubble sort.

from random import randint

def bubble_sort(unsorted: list):
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

def merge_sort(unsorted_list):
    pass

def random_list(Nelements):
    '''
    Generate a list of random integers (0-99) that has `Nelements` number of
    elements.
    '''
    output = []
    for i in range(Nelements):
        output.append(randint(0,99))
    return output

print(bubble_sort(random_list(20)))