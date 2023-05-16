#4. Construa um método que recebe uma lista encadeada de números inteiros e retorna
#uma lista sem repetições, ou seja, uma lista onde cada número aparece apenas uma vez.
#Exemplo: 12 5 -7 8 5 9 12 1 8 → 12 5 -7 8 9 1

lista = input ('Insira os números (separe com espaços): ').split(' ')

for i in lista:
    while lista.count(i) > 1:
        lista.remove(i)

print(lista)