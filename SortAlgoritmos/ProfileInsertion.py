import InsertionSort
import profile

ns = [10000, 20000, 30000, 40000, 50000]

def selection_sort_test(arr):
    InsertionSort.insertion_sort(arr, len(arr))

profile.profile_algorithm(selection_sort_test, ns, "Insertion Sort")