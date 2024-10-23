NAO_ENCONTRADO = -1
def pesquisa_linear(a, n, x):
    """
    Pesquisa o valor x num array de dimensao n.

    :param a: array
    :param n: dimensao da pesquisa
    :param x: o valor a procurar
    :return: A posição do valor procurado no array, ou um valor
    especial NÃO_ENCONTRADO (0, ou -1, por exemplo) caso não exista.
    """
    resultado = NAO_ENCONTRADO
    for i in range(n):
        if a[i] == x:
            resultado = i
    return resultado


def pesquisa_linear_melhorada(a, n, x):
    """
        Pesquisa o valor x num array de dimensao n.

        :param a: array
        :param n: dimensao da pesquisa
        :param x: o valor a procurar
        :return: A posição do valor procurado no array, ou um valor
        especial NÃO_ENCONTRADO (0, ou -1, por exemplo) caso não exista.
        """
    for i in range(n):
        if a[i] == x:
            return i
    return NAO_ENCONTRADO


def pesquisa_linear_com_sentinela(a, n, x):
    """
        Pesquisa o valor x num array de dimensao n.

        :param a: array
        :param n: dimensao da pesquisa
        :param x: o valor a procurar
        :return: A posição do valor procurado no array, ou um valor
        especial NÃO_ENCONTRADO (0, ou -1, por exemplo) caso não exista.
        """
    ultimo = a[n-1]
    a[n-1] = x
    i = 0
    while a[i] != x:
        i = i + 1
    a[n-1] = ultimo
    if i < n or a[n-1] == x:
        return i
    else:
        return NAO_ENCONTRADO
