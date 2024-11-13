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
import bsearch
import lsearch
import time
import profile
def profile_algorithm(func, arr, target, shold_sort=False):
    """
    Perfil de execucao de um algoritimo de pesquisa
    :param func: Funcao de pesquisa
    :param arr: Lista de elementos
    :param target: Elemento a ser procurado
    :param shold_sort: Indica se o array deve ser ordenado
    :return: Tempo de execucao
    """
    if shold_sort:
        arr.sort()
    start_time = time.time()
    func(arr, target)
    end_time = time.time()
    return end_time - start_time
if __name__=="__main__":
    arr = [i for i in range(100000)]
    target = 999999
    time_linear = profile_algorithm(lsearch.linear_search, arr, target)
    time_binary = profile_algorithm(bsearch.binary_search, arr, target, shold_sort=True)
    print(f"Tempo de execucao de pesquisa linear: {time_linear:.5f} segundos")
    print(f"Tempo de execucao de pesquisa binária: {time_binary:.5f} segundos")