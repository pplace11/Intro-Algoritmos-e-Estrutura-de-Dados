# Curso: Desenvolvimento para a Web e Dispositivos Móveis
#
# UC: Algoritmos e Estrutura de Dados
#
# Nome: Pedro Place
#
# Número: 22404914
#
# Data: 10/30/2024
#
def merge_sort(arr, p, u):
    """
    Merge Sort Algorithm

    :param arr: Array to sort.
    :param p: Index of first position to sort.
    :param u: Index of last position to sort.
    :return: Sorted array.
    """
    if p >= u:
        return
    else:
        m = (p + u) // 2
        merge_sort(arr, p, m)
        merge_sort(arr, m + 1, u)
        merge(arr, p, m, u)
def merge(arr, p, m, u):
    """
    Auxiliary function for "conquer" pass in merge sort.

    :param arr: Array to sort.
    :param p: Index of first position.
    :param m: Index of middle position.
    :param u: Index of last position.
    :return: The merged array, already sorted.
    """
    n1 = m - p + 1
    n2 = u - m
    left = [0] * n1
    right = [0] * n2
    # Copy left array
    for i in range(n1):
        left[i] = arr[p + i]
    # Copy right array
    for i in range(n2):
        right[i] = arr[m + 1 + i]
    i = j = 0
    k = p
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # Copy remaining elements of left array if any
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    # Copy remaining elements of right array if any
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
if __name__ == '__main__':
    import random
    LIST_LEN = 30
    arr = random.sample(range(1, LIST_LEN + 1), LIST_LEN)
    print("Array desordenado: ")
    for item in arr:
        print(item, end=" ")
    merge_sort(arr, 0, len(arr) - 1)
    print("\nArray ordenado: ")
    for item in arr:
        print(item, end=" ")