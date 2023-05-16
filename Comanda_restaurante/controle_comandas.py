#Função ara o MENU

def menu():
    print(" --------- MENU ----------")
    print( "" )
    print("Selecione uma das opções abaixo: ")
    print(" 1.Adicionar pedido:")
    print("2. Resumo comanda")
    print("3. Dividir Conta")
    print("4. Remover Comanda")
    print("5. Sair")

def adicionarpedido(mesa, produto, preco):
    with open (f"comanda_{mesa}.txt,""a") as arquivo: #criando um novo objeto chamado arquivo
    
      