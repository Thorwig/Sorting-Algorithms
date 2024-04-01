import random

def quicksort(list: list[int]) -> list[int]:
    if len(list) <= 1:
        return list
    pivot = list[random.randint(0, len(list)-1)]
    less_than_pivot = [x for x in list if x <= pivot]
    more_than_pivot = [x for x in list if x > pivot]
    return quicksort(less_than_pivot) + quicksort(more_than_pivot)