from bubblesort import bubble
from selection import selection
from insertion import insertion
from quicksort import quicksort
from mergesort import mergesort


def test_array(algorithm):
    test_cases = [
        [2, 4, 3, 1],
        [5, 3, 8, 6, 7, 2],
        [],
        [1],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    for test_case in test_cases:
        print(algorithm(test_case))


if __name__ == "__main__":
    if input("Do you want to test all algorithms? (y/n): ") == 'y':
        test_array(bubble)
        test_array(selection)
        test_array(insertion)
        test_array(quicksort)
        test_array(mergesort)
    else:
        if input("Do you want to test bubble sort? (y/n): ") == 'y':
            test_array(bubble)
        if input("Do you want to test selection sort? (y/n): ") == 'y':
            test_array(selection)
        if input("Do you want to test insertion sort? (y/n): ") == 'y':
            test_array(insertion)
        if input("Do you want to test quick sort? (y/n): ") == 'y':
            test_array(quicksort)
        if input("Do you want to test merge sort? (y/n): ") == 'y':
            test_array(mergesort)
    print("Thank you for testing!")
