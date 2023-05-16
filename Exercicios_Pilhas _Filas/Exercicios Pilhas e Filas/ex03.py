#3. Escreva um programa que implemente uma fila circular utilizando uma lista dinâmica.
#O programa deve ser capaz de inserir, remover e informar o tamanho da fila em um dado momento.

lista = []
continuar = "sim"

#Inserir itens
while continuar == "sim":
  
  lista.append(input("Digite um nome: "))
  continuar = input("Deseja continuar? (sim/não): ")

#Mostrar lista
print(lista, '\n')
continuar = "sim"

#Remover itens
while continuar == "sim":
  
  print(f'Removendo {lista[0]} da lista...\n')
  lista.pop(0)
  
  print(lista)
  continuar = input("Deseja continuar? (sim/não): ")

#Informar tamanho
print(f'Tamanho da lista: {len(lista)} itens.')