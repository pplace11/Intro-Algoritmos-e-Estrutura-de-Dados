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
import SelectionSort
import profile

ns = [10000, 20000, 30000, 40000, 50000]

def selection_sort_test(arr):
    SelectionSort.selection_sort(arr, len(arr))

profile.profile_algorithm(selection_sort_test, ns, 'Selection Sort', False, )
profile.profile_algorithm(selection_sort_test, ns, 'Insertion Sort', False, )
profile.profile_algorithm(selection_sort_test, ns, 'Merge Sort', False, )
profile.profile_algorithm(selection_sort_test, ns, 'Quicksort', False)