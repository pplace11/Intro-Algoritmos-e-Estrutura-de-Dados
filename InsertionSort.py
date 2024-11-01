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
def insertion_sort(arr, n):
    for i in range(1, n-1):
        chave = arr[i]
        j=i-1
        while j>=0 and arr[j]>chave:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=chave
if __name__ == '__main__':
    import random
    LIST_LEN = 30
    arr = random.sample(range(1, LIST_LEN + 1), LIST_LEN)
    print("Array desordenado: ")
    for item in arr:
        print(item, end=" ")
    insertion_sort(arr, len(arr))

    print("\nArray ordenad: ")
    for item in arr:
        print(item, end=" ")