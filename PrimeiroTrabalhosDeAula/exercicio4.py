#  Exercício 4 – Instruções condicionais
#
#Curso: Desenvolvimento para Web e Dispositivo Movel
#
#UC:Algoritmos e Estrutura de Dados
#
#Número:22404914
#Nome: Pedro Place
#Data: 10/16/2024
nota = int(input("Introduz a noto de 0 a 20: "))
if nota >= 18 and nota <= 20:
    print(f'Muito bom')
elif nota >= 15 and nota <= 18:
    print(f"Bom")
elif nota >= 12 and nota <= 15:
    print(f"Satisfaz Bom")
elif nota >= 10 and nota <= 12:
    print(f"Satisfaz")
elif nota >= 0 and nota <= 10:
    print(f"Não Satisfaz")