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
    nome_produto = str(input("Qual produto voce quer remover: "))
    for produto in produtos:
        if produto["nome"] == nome_produto:
            produtos.remove(produto)

            salvar_produtos(produtos)
            print(produto)

def adicionar_produto():
    id = produtos[-1]["id"]
    nome_produto = str(input("Qual o nome do produto que voce quer adicionar: "))
    categoria = str(input("Qual a categoria do produto que voce esta adicionando: "))
    preco = float(input("Qual o preço que voce quer adicionar: "))
    estoque = int(input("Qual a quantidade de estoque que voce quer adicionar: "))
    id += 1
    produto_adicionado = {
        "id": id,
        "nome": nome_produto,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque, 
    }
    produtos.append(produto_adicionado)
    salvar_produtos(produtos)
    print(produtos)



def mudar_estoque():
    usuario = str(input("Qual o nome do produto que voce quer mudar o estoque: "))
    quantidade = float(input("Qual a quantidade que voce quer colocar: "))
    for produto in produtos:
        if produto["nome"] == usuario:
            produto["estoque"] = quantidade
            salvar_produtos(produtos)
            print(produtos)

def buscar_nome():
    usuario = str(input("Qual produto voce quer achar: "))
    for produto in produtos:
        if produto["nome"] == usuario:
            print(produto)

def buscar_id():
    id = int(input("Qual o id que voce quer achar: "))
    for produto in produtos:
        if produto["id"] == id:
            print(produto)

def buscar_categoria():
    categoria = str(input("Qual a categoria que voce quer achar: "))
    for produto in produtos:
        if produto["categoria"] == categoria:
            print(produto)

def mudar_preco():
    usuario = str(input("Qual o produto que voce quer mudar: "))
    preco = float(input("Qual o novo preco que voce quer colocar: "))
    for produto in produtos:
        if produto["nome"] == usuario:
            produto["preco"] = preco
            print(produto)


produtos = carregar_produtos()

while True:
    print("=====Estoque====")

    print("1 - Mostrar o estoque")
    print("2 - remover produto")
    print("3 - adicionar produto")
    print("4 - mudar o estoque")
    print("5 - Buscar por nome")
    print("6 - Buscar por id")
    print("7 - Buscar por categoria")
    print("8 - mudar preço")
    print("0 - Sair do Sistema")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
      mostrar()

    elif opcao == "2":
      remover_produto()

    elif opcao == "3":
      adicionar_produto()
        
    elif opcao == "4":
        mudar_estoque()
    
    elif opcao == "5":
        buscar_nome()
    
    elif opcao == "6":
        buscar_id()
    
    elif opcao == "7":
        buscar_categoria()

    elif opcao == "8":
        mudar_preco()
    
    elif opcao == "0":
        print("Saindo do Sistema...")
        break
    else:
        print("opcao invalida, tente novamente!")
        break