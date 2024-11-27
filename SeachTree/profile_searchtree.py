# Curso: Desenvolvimento para a Web e Dispositivos Móveis
#
# UC: Algoritmos e Estrutura de Dados
#
# Nome: Pedro Place
#
# Número: 22404914
#
# Data: 11/27/2024
#

import searchtree
import profile
import random

atree = None

def setup_random_tree(n):
    """
    Cria uma árvore binária de pesquisa com n nós, inserindo valores aleatórios.

    Gera uma lista aleatória de números de 1 a n e insere cada número na árvore.
    A ordem aleatória de inserção visa criar uma árvore balanceada.

    Args:
        n: Número de nós da árvore.
    """
    # ... resto do código
    global atree

    atree = None

    # Gerar uma lista aleatória de números entre 1 e n.
    rlist = random.sample(range(1, n+1), n)

    # Inserir a lista na árvore.
    for item in rlist:
        if atree is None:
            atree = searchtree.SearchTree(item)
        else:
            atree.insert_i(item)

def setup_ordered_tree(n):
    """
    Cria uma árvore binária de pesquisa com n nós, inserindo valores em ordem crescente.

    Gera uma lista ordenada de números de 1 a n e insere cada número na árvore.
    A ordem crescente de inserção resulta em uma árvore degenerada.

    Args:
        n: Número de nós da árvore.
    """
    # ... resto do código
    global atree

    atree = None

    # Gerar uma lista ordenada de números entre 1 e n.
    olist = list(range(1, n+1))

    # Inserir a lista na árvore.
    for item in olist:
        if atree is None:
            atree = searchtree.SearchTree(item)
        else:
            atree.insert_i(item)

def test_tree(n):
    """
    Realiza 10000 buscas por um valor inexistente na árvore para medir o tempo de execução.

    A busca por um valor inexistente garante que a busca percorrerá toda a altura da árvore.

    Args:
        n: Número de nós da árvore.
    """
    # ... resto do código
    global atree

    for i in range(1, 10000):
        atree.exists_i(n)     # Pesquisa valor não existente

# Esperamos que o algoritmo seja O(lg n)
profile.profile_algorithm(algorithm=test_tree,
                          input_sizes=[100000, 200000, 300000, 400000, 500000],
                          algorithm_name="Árvores de Pesquisa Binária - Pesquisa em árvore com valores inseridos aleatóriamente.",
                          use_number_list=False,
                          setup=setup_random_tree,
                          adjust_for_length=False)

# Na prática a árvore será uma lista, pelo que esperamos que o algoritmo seja O(n)
profile.profile_algorithm(algorithm=test_tree,
                          input_sizes=[100000, 200000, 300000, 400000, 500000],
                          algorithm_name="Árvores de Pesquisa Binária - Pesquisa em árvore com valores inseridos por ordem.",
                          use_number_list=False,
                          setup=setup_ordered_tree,
                          adjust_for_length=False)
