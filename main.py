import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

def mostrar():
    print(produtos)

def remover_produto():
    nome_produto = input("Qual produto voce quer remover: ")
    for produto in produtos:
        if produto["nome"] == nome_produto:
            produtos.remove(produto)
            print(produto)

def adicionar_produto():
    nome_produto = input("Qual o nome do produto que voce quer adicionar: ")

produtos = carregar_produtos()


while True:
    print("=====Estoque====")

    print("1 - Mostrar o estoque")
    # print("2 - saida do estoque")
    # print("3 - entrada do estoque")
    print("3 - Remover produto")
    print("4 - Adicionar produto")
    print("5 - Buscar por nome")
    print("6 - Buscar por id")
    print("7 - Buscar por categoria")
    print("8 - Buscar por quantidade no estoque")
    print("0 - Sair do Sistema")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
      mostrar()

    elif opcao == "2":
      remover_produto()

    elif opcao == "3":
        
        
    elif opcao == "4":
    
    elif opcao == "5":
    
    
    elif opcao == "6":
    
    elif opcao == "7":
    
    elif opcao == "0":
        print("Saindo do Sistema...")
        break
    else:
        print("opcao invalida, tente novamente!")
        break