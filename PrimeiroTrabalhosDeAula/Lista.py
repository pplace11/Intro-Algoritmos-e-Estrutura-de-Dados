# Lista em Python
#
#Curso: Desenvolvimento para Web e Dispositivo Movel
#
#UC:Algoritmos e Estrutura de Dados
#
#Número:22404914
#Nome: Pedro Place
#Data: 10/16/2024
nomes = ['Manuel', 'Maria', 'Sara', 'Francisco']
outra = ['maria', 33, True, 3.4]
terceira = [1, 2, 3, 4, 5, 6]

print(f"O Número de nomes na lista: {len(nomes)}")
print(f"O segundo nome na lista é: {nomes[1]}")
print(f"Os nomes a partir do segundo na lista sao: {nomes[1:]}")
print(f"O terceiro nome na lista é: {nomes[2:3]}")
print(f"Os nomes por ordem alfabeticas: {nomes.sort()}")
print("Maria" in nomes)
print("Marina" in nomes)
print(outra)
print(f"O terceiro nome na lista é: {nomes[:3]}")

print([2 * x for x in terceira])     # outra lista com dobros
print([x for x in terceira if x % 2 == 0])   #sublista só com pares

