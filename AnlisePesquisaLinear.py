import profile
import PesquisaLinear

dim_n = [1000000, 2000000, 3000000, 4000000, 5000000]

def teste_pesquisa_linear(a):
    PesquisaLinear.pesquisa_linear(a, len(a), 33)
profile.profile_algorithm(teste_pesquisa_linear,
                            dim_n,
                        "Pesquisa Linear",
                          can_repeat=False)
def teste_pesquisa_linear_melhorada(a):
    PesquisaLinear.pesquisa_linear_melhorada(a, len(a), 33)
profile.profile_algorithm(teste_pesquisa_linear_melhorada,
                            dim_n,
                        "Pesquisa Linear Melhorada",
                          can_repeat=False)
def teste_pesquisa_linear_com_sentinela(a):
    PesquisaLinear.pesquisa_linear_com_sentinela(a, len(a), 33)
profile.profile_algorithm(teste_pesquisa_linear_com_sentinela,
                            dim_n,
                        "Pesquisa Linear com Sentinela",
                          can_repeat=False)