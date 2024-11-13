#  Exercício 5 – Instruções condicionais
#
#Curso: Desenvolvimento para Web e Dispositivo Movel
#
#UC:Algoritmos e Estrutura de Dados
#
#Número:22404914
#Nome: Pedro Place
#Data: 10/16/2024
def calcula_custo_agua(num_m3):
    # Preços por escalão
    preco_escalão1 = 0.4203
    preco_escalão2 = 0.7860
    preco_escalão3 = 1.8499
    preco_escalão4 = 2.3543
    # Quota de Serviço fixa
    quota_servico = 5.80
    # Inicializa o custo total com a Quota de Serviço
    custo_total = quota_servico
    # Calcula o custo por escalão
    if num_m3 <= 5:
        custo_total += num_m3 * preco_escalão1
    elif num_m3 <= 15:
        custo_total += 5 * preco_escalão1 + (num_m3 - 5) * preco_escalão2
    elif num_m3 <= 25:
        custo_total += 5 * preco_escalão1 + 10 * preco_escalão2 + (num_m3 - 15) * preco_escalão3
    else:
        custo_total += 5 * preco_escalão1 + 10 * preco_escalão2 + 10 * preco_escalão3 + (num_m3 - 25) * preco_escalão4
    return custo_total
# Função para testar o cálculo
def teste():
    consumos_teste = [4.5, 10, 20, 30]
    for consumo in consumos_teste:
        print(f"Consumo: {consumo} m3 - Custo: {calcula_custo_agua(consumo):.2f}€")


teste()
