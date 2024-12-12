#CODIGO DO CONTROLE DE ESTOQUE

import json
import interface

estoque_produtos = "estoque.json"



def analisar_estoque():
    try:
        with open(estoque_produtos, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def escrever_estoque(estoque):
    with open(estoque_produtos, "w") as file:
        json.dump(estoque, file, indent=4)


def adicionar_estoque(estoque):
    nome = input("Produto: ").lower()
    preco = float(input("Valor do produto: "))
    quantidade = int(input("Quantidade: "))
    if nome in estoque:
        estoque[nome]["quantidade"] += quantidade
    else:
        estoque[nome] = {"quantidade": quantidade, "preco": preco}
    print(f"O item '{nome}' adicionado/atualizado com sucesso.")


def retirar_estoque(estoque):
    if not (estoque):
        print("Esse Item não está no estoque.")
        return
    nome = input("Digite o nome do item a ser removido:").lower()
    if nome in estoque:
        confirmacao = input(
            "Tem certeza de que vai remover o item '{nome}'? (s/n): ").lower()
        if confirmacao == "s":
            del estoque[nome]
            escrever_estoque(estoque)
            print(f"O item foi removido com sucesso.")
        else:
            print("A remoção foi cancelada")
    else:
        print(f"O item '{nome}' não foi encontrado no estoque")


def editar_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return

    nome = input("Qual item você deseja editar? ").lower()
    if nome in estoque:
        print(f"Informações atuais de '{nome}':")
        print(f"Quantidade: {estoque[nome]['quantidade']}")
        print(f"Preço: R$ {estoque[nome]['preco']:.2f}")

        print("\nO que você deseja editar?")
        print("1. Quantidade")
        print("2. Preço")
        print("3. Nome")
        print("4. Ambos")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nova_quantidade = int(input("Digite a nova quantidade: "))
            estoque[nome]['quantidade'] = nova_quantidade
            print(f"A quantidade de '{nome}' foi atualizada para {nova_quantidade}.")
            
        elif opcao == "2":
            novo_preco = float(input("Digite o novo preço: "))
            estoque[nome]['preco'] = novo_preco
            print(f"O preço de '{nome}' foi atualizado para R$ {novo_preco:.2f}.")
            
        elif opcao == "3":
            novo_nome = input("Digite o novo nome: ").lower()   
            if novo_nome in estoque:
                print(f"Já existe um item chamado '{novo_nome}' no estoque escolha outro nome. ")
            else:
                estoque[novo_nome] = estoque.pop(nome)    
            print(f"O item '{nome}' foi atualizado para {novo_nome}.")
            
        elif opcao == "4":
            nova_quantidade = int(input("Digite a nova quantidade: "))
            novo_preco = float(input("Digite o novo preço: "))
            estoque[nome]['quantidade'] = nova_quantidade
            estoque[nome]['preco'] = novo_preco
            print(f"As informações de '{nome}' foram atualizadas: {nova_quantidade} unidades, R$ {novo_preco:.2f} cada.")
        else:
            print("Opção inválida. Nenhuma alteração foi feita.")
        escrever_estoque(estoque)  # Atualiza o arquivo com as mudanças
    else:
        print(f"O item '{nome}' não foi encontrado no estoque.")



def buscar_estoque(estoque):
    if not (estoque):
        print("Estoque está vazio.")
    else:
        for nome, dados in estoque.items():
            print(f"{nome}: {dados['quantidade']} unidades, R$ {dados['preco']:.2f} cada")


def menu():
    estoque = analisar_estoque()
    while True:
        print("\n--- Controle de Estoque ---")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Editar item")
        print("4. Exibir estoque ")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_estoque(estoque)
            escrever_estoque(estoque)
            
        elif opcao == "2":
            retirar_estoque(estoque)
            
        elif opcao == "3":
            editar_estoque(estoque)
            
        elif opcao == "4":
            buscar_estoque(estoque)
                     
        elif opcao == "5":
            print("Saindo...")
            break
    else:
        print("Opção inválida, tente novamente.")


menu()
