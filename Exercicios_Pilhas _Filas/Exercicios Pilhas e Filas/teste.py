#6. Uma pequena empresa de logística pretende implementar um porto seco para armazenar
#containers e precisa para um programa simples para gerenciar seu porto.

#Dado o tamanho da empresa, essa possui apenas 4 locais onde pode empilhar os containers
#e seu equipamento permite empilhar no máximo 3 containers.

#Por política da empresa, um novo container deve ser colocado no local com a pilha mais baixa disponível
#(se mais de um local tiver a mesma quantidade de containers, tanto faz em que pilha será adicionado).

# Cada container é adicionado a partir de um código informado e o sistema não pode
#permitir códigos repetidos. Para remoção também é preciso informar o código
#do container, mas o mesmo somente será removido se estiver no topo da pilha.

#O algoritmo deve mostrar as seguintes mensagens:
#a) Codigo invalido!: quando for fornecido um valor já existe no momento de inserção e
    #quando for fornecido um valor não existente no momento de remoção.
#b) Impossivel empilhar!: quando não for mais possível adicionar containers nas pilhas.
#c) Impossivel desempilhar!: quando não for possível remover um container, ou por não existir
    #mais containers ou por ele não estar no topo da pilha.

#Apresente uma proposta de solução para o problema acima enunciado!

pilha1, pilha2, pilha3, pilha4 = [], [], [], []
pilhas = [pilha1, pilha2, pilha3, pilha4]
containers = []

def ocupacaoPilhas():
    ocupacao = [len(pilha1), len(pilha2), len(pilha3), len(pilha4)]
    return(ocupacao)


while True:
    
  menu = ['1 - Adicionar Container', '2 - Remover Container', '3 - Ver pilhas', '4 - Sair']
  
  for item in menu:
    print(item)
      
  resposta = input('Opção: ')
  
  
  match resposta:
    
    #Adicionar Container
    case '1':
      
      #Verificando se as pilhas não estão cheias
      if sum(ocupacaoPilhas()) != (len(pilhas) * 3):
        
        cont = 0
        container = input('\nCódigo do Container: ')
        
        for pilha in pilhas:
          if container not in pilha:
            cont += 1
        
        if cont == len(pilhas):
                  
          ocupacao = ocupacaoPilhas()
          menorPilha = min(ocupacao)
              
          idx_menorPilha = ocupacao.index(menorPilha)
          pilhas[idx_menorPilha].append(container)
          containers.append(container)
          
          print(f'Container {container} adicionado à pilha {idx_menorPilha + 1}!\n')
            
        else:
          print('Código inválido! Esse container já está em uma pilha.\n')
          
      else:
          print('\nImpossivel empilhar! As pilhas atingiram a capacidade máxima.\n')
          
    
    #Remover Container
    case '2':
      
      #Verificando se as pilhas não estão vazias
      if sum(ocupacaoPilhas()) != 0:
      
        cont = 0
        container = input('\nCódigo do Container: ')
        
        for pilha in pilhas:
          if container in pilha:
            if len(pilha) == (pilha.index(container) + 1):
              
              idx_pilha = pilhas.index(pilha)
              pilha.remove(container)
              containers.remove(container)
              
              print(f'Container {container} removido da pilha {idx_pilha + 1}!\n')
            
            else:
              print('Impossível desempilhar! Esse container não se encontra no topo da pilha.\n')
              
          else:
            cont += 1
        
        if cont == len(pilhas):
          print('Código inválido! Esse container não está em nenhuma pilha.\n')
          
      else:
        print('\nImpossível desempilhar! Não há containers empilhados.\n')
    
    
    #Ver pilhas
    case '3':
      
      print('\n'
            f'Pilha 1: {pilha1}\n'
            f'Pilha 2: {pilha2}\n'
            f'Pilha 3: {pilha3}\n'
            f'Pilha 4: {pilha4}\n')
    
    
    #Sair
    case '4':
      
      print('\nAté logo!')
      break
    
    
    #Opção inválida
    case _:
      
      print('\nOpção inválida!\n')
