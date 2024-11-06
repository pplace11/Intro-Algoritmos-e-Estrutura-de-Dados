# Curso: Desenvolvimento para a Web e Dispositivos Móveis
#
# UC: Algoritmos e Estrutura de Dados
#
# Nome: Pedro Place
#
# Número: 22404914
#
# Data: 11/06/2024
#
import sys


# Nó de uma Lista Simplemente Ligada (LSL). Deve ser alterado consoante o tipo de lista desejado.
class Node:

    def __init__(self, data=None, next=None):
        """
        Construtor de um nó de uma LSL.
        Inicializa os campos do nó.

        :param data: os dados a armazenar no nó.
        :param next: o próximo nó na lista. None se existir nenhum.
        """
        self.data = data
        self.next = next


# Lista Simplesmente Ligada (LSL).
# Nome e comentários devem ser alterados consoante o tipo de lista a implementar.
class SinglyLinkedList:
    """
    Classe que representa uma lista simplesmente ligada.

    Notas:
    1. Os procedimentos declarados numa classe chamam-se métodos.
    2. Todos os métodos têm no mínimo um parâmtro "self" que representa a instância (objeto/variável) no contexto da
       qual a invocação foi feita.
    3. Podem criar-se variáveis do tipo definido por uma classe usando "var = NomeDaClasse()".
       Esta operação invoca o construtor da classe (método __init__()).
    4. As variáveis associadas a cada instância de uma classe chamam-se propriedades e acedem-se usando
       "self.nome_da_propriedade".
    5. Ver a função main() no final do ficheiro para mais exemplos de como a classe é usada.
    """
    def __init__(self):
        """
        Construtor de uma LSL.
        Inicializa os campos da lista.
        """
        self._head = None
        self._tail = None
        self._size = 0
    def insert_before(self, data, node):
        """
        Insere um novo nó, antes do nó especificado.
        O algoritmo usado garante que esta operação é O(1).

        :param data: dados a inserir.
        :param node: o nó, existente na lista, antes do qual inserir.
        :return: o novo nó, que foi inserido na lista.
        """
        if node:
            clone = Node(node.data, node.next)
            node.data = data
            node.next = clone
            if clone.next is None:
                self._tail = clone
            self._size += 1
            return node
        else:
            raise RuntimeError("o no nao existe!")

    def insert_after(self, data, node):
        """
        Insere um novo nó, após o nó especificado.
        Se, em vez de um nó, for especificada a própria lista, insere à cabeça.

        :param data: dados a inserir.
        :param node: o nó, existente na lista, depois do qual inserir.
        :return: o novo nó, que foi inserido na lista.
        """
        if node != self:
            new_node = Node(data, node.next)
            node.next = new_node
            if new_node.next is None:
                self._tail = new_node
        else:
            new_node = Node(data, self._head)
            self._head = new_node
            if new_node.next is None:
                self._tail = new_node
        self._size += 1
        return new_node

    def insert_head(self, data):
        """
        Insere um novo nó, à cabeça da LSL.

        :param data: dados a inserir.
        :return:  o novo nó, que foi inserido na lista.
        """
        if self._head:
            new_node = Node(data, self._head)
            self._head = new_node
        else:
            new_node = Node(data)
            self._head = new_node
            self._tail = new_node
        self._size += 1
        return new_node

    def insert_tail(self, data):
        """
        Insere um novo nó, no fim da LSL.

        :param data: dados a inserir.
        :return: o novo nó, que foi inserido na lista.
        """
        new_node = Node(data)
        current = self._tail
        current.next = new_node
        self._tail = new_node
        self._size += 1
        return new_node

    def remove_head(self):
        """
        Remove o nó à cabeça da lista.

        :return: None
        """
        if self._head:
            first_node = self._head
            self._head = first_node.next
            self._size -= 1
            if self._head is None:
                self._tail = self._head
        else:
            raise RuntimeError("A lista está vazia!")

    def remove_tail(self):
        """
        Remove o nó na cauda da lista.

        :return: None
        """
        if self._head:
            if self._head == self._tail:
                self._head = self._tail = None
            else:
                current = self._head
                while current.next:
                    prev = current
                    current = current.next
                prev.next = None
                self._tail = prev
            self._size -= 1
        else:
            raise RuntimeError("A lista está vazia!")

    def remove_after(self, node):
        """
        Remove o nó após o nó especificado.
        Se, em vez de um nó, for especificada a própria lista, remove à cabeça.

        :param node: o nó depois do qual remover.
        :return: None.
        """
        if node != self:
            if node.next:
                node.next = node.next.next
        else:
            if self._head:
                self._head = self._head.next
                if self._head is None:
                    self._tail = self._head
        self._size -= 1

    def remove(self, node):
        """
        Remove o nó especificado da lista.
        O algoritmo garante que esta operação é O(1) para todos os nós, exceto o último.

        :param node: o nó a remover.
        :return: None
        """
        if node:
            if node.next:
                node.data = node.next.data
                node.next = node.next.next
                if node.next is None:
                    self._tail = node
                self._size -= 1
            else:
                if self._tail == node:
                    self.remove_tail()
                else:
                    raise RuntimeError("O no nao pertence a lista!")
        else:
            RuntimeError("O no nao existe!")

    def head(self):
        """
        Devolve o nó à cabeça da lista.

        :return: O nó na cabeça da lista ou None se a lista está vazia.
        """
        return self._head

    def tail(self):
        """
        Devolve o nó na cauda da lista.

        :return: O nó na cauda da lista ou None se a lista está vazia.
        """
        return self._tail
        pass

    def size(self):
        """
        Devolve o número de nós presentes na lista.

        :return: número de nós presentes na lista.
        """
        return self._size

    def print(self):
        """
        Escreve o conteúdo aa lista.

        :return: None.
        """
        pass


def main() -> int:
    """
    Um teste básico para validar a implementação de uma LSL existente neste módulo.
    As instruções assert terminam a execução caso a expressão Booleana especificada seja falsa.

    :return: 0 se os testes executaram com sucesso.
    """

    def assert_head_tail_path(ll):
        """
        Confirmar que, percorrendo a lista a partir da cabeça, se chega à cauda.

        :param ll: lista
        :return: None
        """
        current = ll.head()
        print("Head->", end=" ")
        while current:
            prev = current
            print(current.data, end=" ")
            current = current.next
        print()
        assert (ll.head() is None and ll.tail() is None) or ll.tail() == prev

    print("+-----------------------------------------------------------------+")
    print("| Teste à implemementação de uma LSL existente neste módulo       |")
    print("+-----------------------------------------------------------------+")

    # Criação da lista
    ll = SinglyLinkedList()
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #  tail -> +----+
    #  head -> | 33 |-->None
    #          +----+
    ll.insert_head(33)
    assert ll.size() == 1
    assert ll.head().data == 33
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 34 |-->| 33 |-->None
    #          +----+   +----+
    ll.insert_head(34)
    assert ll.size() == 2
    assert ll.head().data == 34
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 34 |-->| 33 |-->None
    #          +----+   +----+   +----+
    ll.insert_head(35)
    assert ll.size() == 3
    assert ll.head().data == 35
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+
    ll.insert_tail(36)
    assert ll.size() == 4
    assert ll.head().data == 35
    assert ll.tail().data == 36
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 37 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+   +----+
    ll.insert_after(37, ll._head)
    assert ll.size() == 5
    assert ll.head().data == 35
    assert ll.tail().data == 36
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 37 |-->| 38 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+   +----+   +----+
    current = ll.head()
    while current.data != 37 and current.next:
        current = current.next
    ll.insert_after(38, current)
    assert ll.size() == 6
    assert ll.head().data == 35
    assert current.next.data == 38
    assert ll.tail().data == 36
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 37 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+   +----+
    ll.remove_after(current)
    assert ll.size() == 5
    assert ll.head().data == 35
    assert current.next.data != 38
    assert ll.tail().data == 36
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+ <- tail
    #  head -> | 37 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+
    ll.remove_head()
    assert ll.size() == 4
    assert ll.head().data == 37
    assert ll.tail().data == 36
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+ <- tail
    #  head -> | 37 |-->| 34 |-->| 33 |-->None
    #          +----+   +----+   +----+
    ll.remove_tail()
    assert ll.size() == 3
    assert ll.head().data == 37
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 34 |-->| 33 |-->None
    #          +----+   +----+
    ll.remove_head()
    assert ll.size() == 2
    assert ll.head().data == 34
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+ <- tail
    #  head -> | 33 |-->None
    #          +----+
    ll.remove_head()
    assert ll.size() == 1
    assert ll.head().data == 33
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 39 |-->| 33 |-->None
    #          +----+   +----+
    ll.insert_before(39, ll.head())
    assert ll.size() == 2
    assert ll.head().data == 39
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+ <- tail
    #  head -> | 39 |-->| 40 |-->| 33 |-->None
    #          +----+   +----+   +----+
    ll.insert_before(40, ll.tail())
    assert ll.size() == 3
    assert ll.head().data == 39
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 39 |-->| 33 |-->None
    #          +----+   +----+
    current = ll.head().next
    ll.remove(current)
    assert ll.size() == 2
    assert ll.head().data == 39
    assert ll.head().next.data != 40
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+ <- tail
    #  head -> | 39 |-->None
    #          +----+
    ll.remove(ll.tail())
    assert ll.size() == 1
    assert ll.head().data == 39
    assert ll.tail().data == 39
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #  tail -> None
    #  head -> None
    #
    ll.remove(ll.head())
    assert ll.size() == 0
    assert ll.head() is None
    assert ll.tail() is None
    assert_head_tail_path(ll)

    print("+----------------------------------------------------------------+")
    print("| Todos os testes terminaram com sucesso!                        |")
    print("+----------------------------------------------------------------+")

    return 0


if __name__ == "__main__":
    sys.exit(main())