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
def binary_search(arr, target):
    """
    Pesquisa binaria em array orednado
    :param arr: Lista ordenada de elementos
    :param target: Elemento a ser procurado
    :return: Índice do elemento se encontrado, caso contrário -1
    """
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid]<target:
            low = mid +1
        elif arr[mid]>target:
            high = mid -1
        else:
            return mid
    return -1