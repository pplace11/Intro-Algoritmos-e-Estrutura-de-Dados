# Curso: Desenvolvimento para a Web e Dispositivos Móveis
#
# UC: Algoritmos e Estrutura de Dados
#
# Nome: Pedro Place
#
# Número: 22404914
#
# Data: 12/04/2024
#

class BST:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.data = value

    def build_BST(self, value):
        if self.data == value:
            return
        if self.data is None:
            self.data = value
        elif value < self.data:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.build_BST(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.build_BST(value)

def main():
    """
    Função principal para testar a implementação da árvore binária de busca.
    """
    import random
    from drawtree import drawTree

    lista = [15, 10, 20, 8, 8, 12, 18, 25]
    print("Lista original:", lista)
    print("Lista ordenada:", sorted(lista))
    bst = BST()
    for num in lista:
        bst.build_BST(num)
    drawTree(bst)

if __name__ == "__main__":
    main()