# Importando bibliotecas
import os
import time
from listar import listar

# Lista para armazenar as informacoes do usuario e pedido
informacoes_pessoais = []
informacoes_pedido = {
    "Sanduiche": None,
    "Bebida": None,
}
info_endereco = []
info_pagamento = []

sanduiches=("Sanduiche de Carne Assada", "Sanduiche de Pernil", "Sanduiche de Rosbife")
bebidas=("Suco de limão", "Suco de limão com morango", "Coca cola")
pagamentos=("Débito", "Crédito", "Pix", "Dinheiro")

# Apresentação do nosso Bot
def apresentacao():
    print("-" * 40)
    saudacao = "\n "+"~"*3+"  O MELHOR SANDUÍCHE DA CIDADE  "+"~"*3
    print("~" * 8, "BEM VINDO AO SANDUREI", "~" * 8, saudacao)
    print("-" * 40)

# Começar o atendimento
def menu1():
    opcao = 0

    while opcao != "5":
        os.system('cls')
        print("É um prazer " + nome, "vamos continuar com o seu atendimento!")
        listar(("Escolha seu Sanduíche.", "Escolha sua Bebida.", "Qual a Forma de Pagamento?", "Finalizar Pedido.", "Sair."))
        #print("1. Escolha seu Sanduiche. \n2. Escolha sua Bebida. \n3. Qual a Forma de Pagamento? \n4. Finalizar Pedido. \n5. Sair.")
        opcao = input("Qual opção deseja? ")

        if opcao == "5":
            print("Saindo")
            os.system('cls')
            break

        elif opcao == "4":
            os.system('cls')
            print("Finalizado.")
            time.sleep(1)
            os.system('cls')
            print("Finalizado..")
            time.sleep(1)
            os.system('cls')
            print("Finalizado...")
            time.sleep(1)
            endereco()
            
        elif opcao == "3":
            os.system('cls')
            #print(f"1. Débito. \n2. Crédito. \n3. Pix. \n4. Dinheiro.")
            listar(pagamentos)
            pagamento = input("Qual opção deseja? ")
            info_pagamento.append(pagamento)
            return menu1()

        elif opcao == "2":
            os.system('cls')
            #print("1. Suco de limão. \n2. Suco de limão com morango. \n3. Coca cola")
            listar(bebidas)
            bebida = input("Qual opção deseja? ")
            informacoes_pedido["bebida"]=bebida
            return menu1()
        elif opcao == "1":
            os.system('cls')
            print(sanduiches)
            sanduiche = input("Qual opção deseja? ")
            informacoes_pedido["Sanduiche"] = sanduiche
            return menu1()

        else:
            print("Opção inválida, selecione as opções.")
            return menu1()

# Coletando Informações sobre o Endereço
def endereco():
    print("Agora precisamos saber o seu endereço.")
    endereco1 = input("Qual o seu endereço? ")
    info_endereco.append(endereco1)
    bairro = input("Qual o seu Bairro? ")
    info_endereco.append(bairro)
    referencia = input("Qual o Ponto de Referencia? ")
    info_endereco.append(referencia)
    os.system('cls')
    print("Montando o seu pedido.")
    time.sleep(0.5)
    os.system('cls')
    print("Montando o seu pedido..")
    time.sleep(0.5)
    os.system('cls')
    print("Montando o seu pedido...")
    time.sleep(0.9)
    os.system('cls')
    fechamento()

# Fechamento do pedido com as informações Gerais
def fechamento():
    print(f"Nome: {informacoes_pessoais}\n")
    print(f"Endereço: {info_endereco[0]}\nBairro: {info_endereco[1]}\nReferencia: {info_endereco[2]}")
    print(info_pagamento)
    
    for i in informacoes_pedido:
        print(f"Item: {i}")
    
    input("Correto?")




# Inicio
apresentacao()
nome = input("Seja bem vindo! Qual o seu nome? ")
informacoes_pessoais.append(nome)
menu1()
