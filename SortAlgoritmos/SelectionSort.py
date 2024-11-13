#
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
def selection_sort(arr, arr_length):
    '''
    Selection Sort Algorithm
    :param arr: array to sort
    :param arr_length: array length
    :return: sorted array
    '''
    for i in range(arr_length-1):
        min_index = i
        for j in range(i+1,arr_length):
            if arr[j] < arr[min_index]:
                min_index = j
        # tmp = arr[i]
        # arr[i] = arr[min_index]
        # arr[min_index] = tmp
        arr[i],arr[min_index] = arr[min_index],arr[i]

if __name__ == '__main__':
    import random

    LIST_LEN = 30
    arr = random.sample(range(1, LIST_LEN+1), LIST_LEN)

    print("Array desordenado: ")
    for item in arr:
        print(item, end= " ")

    selection_sort(arr, len(arr))

    print("\nArray ordenado: ")
    for index, item in enumerate(arr):
        assert arr[index] == index + 1, "Sort error!"
        print(item, end=" ")