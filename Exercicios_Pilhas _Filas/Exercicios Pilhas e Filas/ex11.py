#Construa um algoritmo em python que seja capaz de somar somente dois números pares entre 20 e 50 e mostre o resultado

soma = 0
contador = 0

# Percorre os números entre 20 e 50
for num in range(20, 51):
    # Verifica se o número é par
    if num % 2 == 0:
        soma += num
        contador += 1

        # Verifica se encontrou os dois números pares
        if contador == 2:
            break

# Verifica se encontrou dois números pares
if contador == 2:
    print("A soma dos dois números pares entre 20 e 50 é:", soma)
else:
    print("Não há dois números pares entre 20 e 50.")
