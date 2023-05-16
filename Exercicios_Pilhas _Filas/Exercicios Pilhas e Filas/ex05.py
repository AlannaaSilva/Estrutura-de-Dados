#5. Escreva um programa que simule o controle de uma pista de decolagem de aviões em um aeroporto.
#Neste programa, o usuário deve ser capaz de realizar as seguintes tarefas:

#a) Listar o número de aviões aguardando na fila de decolagem;
#b) Autorizar a decolagem do primeiro avião da fila;
#c) Adicionar um avião à fila de espera;
#d) Listar todos os aviões na fila de espera;
#e) Listar as características do primeiro avião da fila.

#Considere que os aviões possuem um nome e um número inteiro como identificador.
#Adicione outras características conforme achar necessário.


espera = []

while True:
    
  menu = ['1 - Ver fila de espera', '2 - Adicionar avião na fila', '3 - Liberar avião', '4 - Sair']
  
  for item in menu:
    print(item)
      
  resposta = input('Opção: ')
  
  
  match resposta:
    
    #Ver fila de espera
    case '1':
      
      print('\nFila de Espera:')
      
      for i in range(len(espera)):
        print(f'{i+1} - {espera[i]}')
        
      print('\n')
        
        
    #Adicionar avião na fila
    case '2':
      
      aviaoNome = input('\nNome: ')
      aviaoNum = (input('Número: '))
      
      aviao = str(aviaoNome)+str(aviaoNum)
      espera.append(aviao)
      
      print(f'Avião {aviao} adicionado à fila de espera!\n')
        
        
    #Liberar avião
    case '3':
      
      opc = input(f'\nDeseja liberar {espera[0]}? (s/n): ').lower()
      
      if opc == 's':
        print(f'{espera[0]} liberado para decolagem!')
        espera.remove(espera[0])
          
      print('\n')
        
    
    #Sair
    case '4':
      
      print('\nAté logo!')
      break
    
    
    #Opção inválida
    case _:
      
      print('\nInsira uma opção válida!\n')
