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

class SearchTree:

    def __init__(self, data=None, left=None, right=None):
        """
        Construtor de uma árvore binária.

        :param data: valor a armazenar no nó.
        :param left: o nó seguinte à esquerda. None se não existir.
        :param right: o nó seguinte à direita. None se não existir.
        """
        self.data = data
        self.left = left
        self.right = right

    def depth(self):
        """
        Calcula a profundidade da árvore (profundidade do nó mais profundo).

        :return: -1 se a árvore não tem nós
                  0 se a árvore apenas tem a raiz
                  n - o número de segmentos entre a raiz e a folha mais profunda.
        """
        if self.data is None:
            return -1
        left_depth = self.left.depth() if self.left else -1
        right_depth = self.right.depth() if self.right else -1
        return 1 + max(left_depth, right_depth)

    def insert_left(self, data):
        """
        Insere nó à esquerda.

        :param data: Valor a guardar no novo nó.
        :return: None
        """
        if self.left is None:
            self.left = SearchTree(data)
        else:
            new_node = SearchTree(data, left=self.left)
            self.left = new_node

    def insert_right(self, data):
        """
        Insere nó à direita.

        :param data: Dados a guardar no novo nó.
        :return: None
        """
        if self.right is None:
            self.right = SearchTree(data)
        else:
            new_node = SearchTree(data, right=self.right)
            self.right = new_node

    def insert(self, data):
        """
        Insere, recursivamente, o valor especificado na posição correta da árvore.

        :param data: valor a adicionar à árvore.
        :return: None
        """
        if data < self.data:
            if self.left is None:
                self.left = SearchTree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = SearchTree(data)
            else:
                self.right.insert(data)
        # Valores iguais são ignorados.

    def insert_i(self, data):
        """
        Insere, iterativamente, o valor especificado na posição correta da árvore.

        :param data: valor a adicionar à árvore.
        :return: None
        """
        current = self
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = SearchTree(data)
                    break
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = SearchTree(data)
                    break
                current = current.right
            else:
                break  # Valores iguais são ignorados.

    def delete(self, data):
        """
        Remove da árvore o nó com o valor especificado.

        :param data: valor a remover.
        :return: A nova raiz da árvore, possivelmente diferente da inicial, depois da remoção.
        """
        if self is None:
            return None
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None:  # Caso de 0 ou 1 filho (à direita).
                return self.right
            elif self.right is None:  # Caso de 1 filho (à esquerda).
                return self.left
            # Caso de 2 filhos: encontrar o menor valor na subárvore direita.
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            self.data = min_larger_node.data
            self.right = self.right.delete(min_larger_node.data)
        return self

    def min(self):
        """
        Devolve o menor valor armazenado na árvore.

        :return: Menor valor na árvore.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    def max(self):
        """
        Devolve o maior valor armazenado na árvore.

        :return: Maior valor na árvore.
        """
        current = self
        while current.right is not None:
            current = current.right
        return current.data

    def exists(self, data):
        """
        Avalia, recursivamente, a existência na árvore do valor especificado.

        :param data: Valor a procurar.
        :return: True se valor existe na árvore.
                 False se valor não existe na árvore.
        """
        if self.data is None:
            return False
        if data == self.data:
            return True
        elif data < self.data:
            return self.left.exists(data) if self.left else False
        else:
            return self.right.exists(data) if self.right else False

    def exists_i(self, data):
        """
        Avalia, iterativamente, a existência na árvore do valor especificado.

        :param data: Valor a procurar.
        :return: True se valor existe na árvore.
                 False se valor não existe na árvore.
        """
        current = self
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def traverse_tree(self, values):
        """
        Percorre (inorder) todos os elementos na árvore.

        :param values: Lista na qual adicionar elementos da árvore, por ordem.
        :return: Lista de valores na árvore (a mesma que é fornecida como parâmetro).
        """
        if self.left:
            self.left.traverse_tree(values)
        values.append(self.data)
        if self.right:
            self.right.traverse_tree(values)
        return values


def main():
    import math
    import random
    from drawtree import drawTree

    MAX_LEN = 30

    rlist = random.sample(range(1, MAX_LEN + 1), MAX_LEN)  # Lista de números por ordem aleatória
    olist = range(1, MAX_LEN + 1)                          # Lista de números por ordem

    print("########################################################################")
    print("#  A testar implementação de Árvore Binária.                           #")
    print("########################################################################")

    #############################################################################
    # Inserir n valores por ordem.                                              #
    #############################################################################
    tree1 = None
    for i in olist:
        if tree1 is None:
            tree1 = SearchTree(i)
        else:
            tree1.insert(i)
    assert tree1.depth() == len(olist) - 1  # Resultado é "lista ligada" com profundidade n - 1.
    assert tree1.max() == max(olist)        # Mínimo da árvore deve ser mínimo inserido
    assert tree1.min() == min(olist)        # Máximo da árvore deve ser máximo inserido

    #############################################################################
    # Assegurar que todos os elementos inseridos estão na lista.                #
    #############################################################################
    for i in olist:
        assert tree1.exists(i)
        assert tree1.exists_i(i)
    assert tree1.traverse_tree([]) == list(olist)   # O resultado da travessia devem ser valores ordenados
    print(f"Tree1 (inorder): {tree1.traverse_tree([])}")
    drawTree(tree1)

    #############################################################################
    # Apagar elementos da lista por uma ordem aleatória        .                #
    #############################################################################
    dlist = random.sample(range(1, MAX_LEN + 1), MAX_LEN)
    for i in dlist:
        tree1 = tree1.delete(i)         # A raiz da lista pode mudar se apagarmos raiz.
        if i != dlist[-1]:
            assert not tree1.exists(i)  # Nó removido não deve estar na árvore.
    assert tree1 is None                # Removido o último elemento, a raiz deve ser None.

    ################################################################################
    # Inserir n valores aleatórios resulta numa árvore com profundidade aleatória. #
    ################################################################################
    tree2 = None
    for i in rlist:
        if tree2 is None:
            tree2 = SearchTree(i)
        else:
            tree2.insert_i(i)           # Nesta árvore inserimos com versão iterativa
    assert math.log(len(rlist), 2) <= tree2.depth() <= len(rlist) - 1
    assert tree2.max() == max(rlist)    # Mínimo da árvore deve ser mínimo inserido
    assert tree2.min() == min(rlist)    # Máximo da árvore deve ser máximo inserido

    #############################################################################
    # Assegurar que todos os elementos inseridos estão na lista.                #
    #############################################################################
    for i in rlist:
        assert tree2.exists(i)
        assert tree2.exists_i(i)
    assert tree2.traverse_tree([]) == list(olist)   # Resultado da travessia devem ser valores por ordem
    print(f"Tree2 (inorder): {tree2.traverse_tree([])}")
    drawTree(tree2)

    #############################################################################
    # Apagar elementos da lista por uma ordem aleatória        .                #
    #############################################################################
    dlist = random.sample(range(1, MAX_LEN + 1), MAX_LEN)
    for i in dlist:
        tree2 = tree2.delete(i)         # A raiz da lista pode mudar se apagarmos a raiz!
        if i != dlist[-1]:
            assert not tree2.exists(i)  # Nó removido não deve estar na árvore.
    assert tree2 is None                # Removido o último elemento a raiz deve ser None.

    print("########################################################################")
    print("#  Testes concluídos com sucesso.                                      #")
    print("########################################################################")


if __name__ == "__main__":
    main()
