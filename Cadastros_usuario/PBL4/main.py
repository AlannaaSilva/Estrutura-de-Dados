#SISTEMA DE CADASTRO 

  #SEÇÕES PRINCIPAIS SÃO IDENTIFICADAS POR COMENTÁRIOS EM CAIXA ALTA.
  #Seções secundárias são identificadas por comentários em caixa baixa.


#IMPORTAÇÕES
import tkinter as tk
from tkinter import ttk
import openpyxl


#FUNÇÕES
def carregarArquivo():
    arquivo = "/Users/caiquemenezes/Documents/VS Code/Aulas/UNDB/Estrutura de Dados/PBL4/people.xlsx"
    workbook = openpyxl.load_workbook(arquivo)
    sheet = workbook.active

    #Lista com todos os dados do arquivo
    listaDados = list(sheet.values)
    print(listaDados)
    
    for nomeColuna in listaDados[0]:
        treeview.heading(nomeColuna, text=nomeColuna)

    for tuplaRegistro in listaDados[1:]:
        treeview.insert('', tk.END, values=tuplaRegistro)


def inserirLinha():
    nome = entryNome.get()
    dataNasc = (entryNasc.get())
    cpf = (entryCPF.get())
    nome_mae = (entryMae.get())
    cep = (entryCEP.get())
    num_end = (entryNumEndereco.get())
    complemento = (entryComplemento.get())
    

    print(nome, dataNasc, cpf, nome_mae, cep, num_end, complemento)

    #Inserir linha no excel
    arquivo = "/Users/caiquemenezes/Documents/VS Code/Aulas/UNDB/Estrutura de Dados/PBL4/people.xlsx"
    workbook = openpyxl.load_workbook(arquivo)
    sheet = workbook.active
    linhaValores = [nome, dataNasc, cpf, nome_mae, cep, num_end, complemento]
    sheet.append(linhaValores)
    workbook.save(arquivo)

    #Inserir linha no tree view
    treeview.insert('', tk.END, values=linhaValores)
    
    #Limpar campos de entrada
    entryNome.delete(0, "end")
    entryNome.insert(0, "Nome Completo")
    
    entryNasc.delete(0, "end")
    entryNasc.insert(0, "Nasc")
    
    entryCPF.delete(0, "end")
    entryCPF.insert(0, "CPF")
    
    entryMae.delete(0, "end")
    entryMae.insert(0, "Mãe")
    
    entryCEP.delete(0, "end")
    entryCEP.insert(0, "CEP")
    
    entryNumEndereco.delete(0, "end")
    entryNumEndereco.insert(0, "Número")
    
    entryComplemento.delete(0, "end")
    entryComplemento.insert(0, "Complemento")


#VISUAL
root = tk.Tk()
root.title('Sistema de Cadastro')


#Tema da Interface
style = ttk.Style(root)
root.tk.call("source", "/Users/caiquemenezes/Documents/VS Code/Aulas/UNDB/Estrutura de Dados/PBL4/forest-dark.tcl")
style.theme_use("forest-dark")


#Frames p/ Disposição dos itens na tela
frame = ttk.Frame(root)
frame.pack()

frameCadastro = ttk.LabelFrame(frame, text="Novo Cadastro")
frameCadastro.grid(row=0, column=0, padx=20, pady=10)


#Entrada de Nome
entryNome = ttk.Entry(frameCadastro, width= 40)
entryNome.insert(0, "Nome Completo")
entryNome.bind("<FocusIn>", lambda e: entryNome.delete('0', 'end'))
entryNome.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")


#Entrada de Data de Nascimento
entryNasc = ttk.Entry(frameCadastro)
entryNasc.insert(0, "Data de Nascimento")
entryNasc.bind("<FocusIn>", lambda e: entryNasc.delete('0', 'end'))
entryNasc.grid(row=1, column=0, padx=5, pady=5, sticky="ew")


#Entrada de CPF
entryCPF = ttk.Entry(frameCadastro)
entryCPF.insert(0, "CPF")
entryCPF.bind("<FocusIn>", lambda e: entryCPF.delete('0', 'end'))
entryCPF.grid(row=2, column=0, padx=5, pady=5, sticky="ew")


#Entrada de Nome da Mãe
entryMae = ttk.Entry(frameCadastro)
entryMae.insert(0, "Nome da Mãe")
entryMae.bind("<FocusIn>", lambda e: entryMae.delete('0', 'end'))
entryMae.grid(row=3, column=0, padx=5, pady=5, sticky="ew")


#Separador
separadorEnd = ttk.Separator(frameCadastro)
separadorEnd.grid(row=4, column=0, padx=(20, 10), pady=(10, 5), sticky="ew")

labelEnd = ttk.Label(frameCadastro, text='Endereço')
labelEnd.grid(row=5, column=0, padx=(20, 10), pady=5, sticky="ew")


#Entrada de CEP
entryCEP = ttk.Entry(frameCadastro)
entryCEP.insert(0, "CEP")
entryCEP.bind("<FocusIn>", lambda e: entryCEP.delete('0', 'end'))
entryCEP.grid(row=6, column=0, padx=5, pady=(5), sticky="ew")


#Entrada de Número
entryNumEndereco = ttk.Entry(frameCadastro)
entryNumEndereco.insert(0, "Número")
entryNumEndereco.bind("<FocusIn>", lambda e: entryNumEndereco.delete('0', 'end'))
entryNumEndereco.grid(row=7, column=0, padx=5, pady=(5), sticky="ew")


#Entrada de Complemento
entryComplemento = ttk.Entry(frameCadastro)
entryComplemento.insert(0, "Complemento")
entryComplemento.bind("<FocusIn>", lambda e: entryComplemento.delete('0', 'end'))
entryComplemento.grid(row=8, column=0, padx=5, pady=(5), sticky="ew")


#Entrada de Botão
button = ttk.Button(frameCadastro, text="Insert", command=inserirLinha)
button.grid(row=9, column=0, padx=5, pady=5, sticky="nsew")


#Janela de Visualização do Arquivo
treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

cols = ("Nome", "Nasc", "CPF", "Mãe", "CEP", "Número", "Complemento")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScroll.set, columns=cols, height=17)

treeview.column("Nome", width=200)
treeview.column("Nasc", width=100)
treeview.column("CPF", width=150)
treeview.column("Mãe", width=200)
treeview.column("CEP", width=150)
treeview.column("Número", width=50)
treeview.column("Complemento", width=150)

treeview.pack()
treeScroll.config(command=treeview.yview)
carregarArquivo()



root.attributes('-fullscreen', True)
root.mainloop()