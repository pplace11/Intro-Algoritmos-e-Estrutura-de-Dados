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
from turtledemo.sorting_animate import partition


def quick_sort(arr, p, u):
    """
    quick sort algorithm
    ----------
    :param arr: array to start
    :param p: index of first position
    :param u: index of last position
    :return: started array
    """
    if p > u:
        return
    else:
        m = partition(arr, p, u)
        quick_sort(arr, p, m -1)
        quick_sort(arr, m + 1, u)
def partition(arr, p,u):
    """
    quick sort algorithm
    ----------
    :param arr: array to start
    :param p: index of first position
    :param u: index of last position
    :return: devolve a posição do pivot!
    """
    m = p
    for k in range(p, u):
        if arr[k] <= arr[u]:
            arr[m],arr[k] = arr[k], arr[m]
            m = m + 1
    arr[m] , arr[u] = arr[u], arr[m]
    return m
if __name__ == '__main__':
    import random

    LIST_LEN = 30
    arr = random.sample(range(1, LIST_LEN + 1), LIST_LEN)

    print("Array desordenado: ")
    for item in arr:
        print(item, end=" ")

    quick_sort(arr, 0, len(arr) - 1)

    print("\nArray ordenado: ")
    for index,item in enumerate(arr):
        assert arr[index] == index + 1, "Sort error!"
        print(item, end=" ")