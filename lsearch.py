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
def linear_search(arr, target):
    """
    Pesquisa linear em um array
    :param arr: Lista de elementos
    :param target: Elemento a ser procurado
    :return: Índice do elemento se encontrado, caso contrário -1
    """
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1