# Curso: Desenvolvimento para a Web e Dispositivos Móveis
#
# UC: Algoritmos e Estrutura de Dados
#
# Nome: Pedro Place
#
# Número: 22404914
#
# Data: 11/13/2024
#
import fila
import pilha

def is_palindrome(str):
    """

    :param str: The string to evaluate.
    :return: True is str is a palindrome. False otherwise
    """
    stk = pilha.StackUsingListEnd()
    q = fila.QueueUsingDeque()

    stripped = "".join(str.lower().split())

    for ch in stripped:
        stk.push(ch)
        q.enqueue(ch)

    while not q.is_empty():
        if stk.pop() != q.dequeue():
            return False
    return True


def main():
    strings = [
        "Pedro"
        "Amor a Roma."
        "O lobo ama o bolo"
    ]
    for s in strings:
        print(f"{s} is a palindrome? {is_palindrome(s)}")


if __name__ == "__main__":
    main()