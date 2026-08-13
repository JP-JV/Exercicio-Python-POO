# 2- objetivo do exercício:
# 	* variáveis
# 	* tipos de dados e conversões
# 	* exceções aritméticas relacionais e logicas
# 	* estruturas de decisões como if e else
# 	* lações de repetição, while ou for
# 	* funções
# 	* estruturas de dados compostas: listas e ou dicionários
# 	* tratamento de erros: try, catch
# 	* classes e objetos

#    descrição:
# você devera criar um sistema simples de cadastro de produtos e compra. 
# O sistema devera permitir que o usuário faça:
# cadastre produtos, visualizar produtos cadastrados, realizar uma compra, calcular o total a pagar, trate entradas invalidas

#   requisitos do programa:
# requisitos funcionais: 
# 1 - classe produto: 
# atributos: nome, endereço
# método: exibir
# 2 - estrutura de dados, usar lista para armazenar os produtos
# 3 - menu:
#  3.1- cadastrar produto
#  3.2- listar produtos
#  3.3- comprar produto
#  3.4- sair

# 4 - cadastro produto:
#  ao ecolher a opção 1:
# solicite o nome do produto
# solicite o preço
# trate os possíveis erros
# crie um objeto da classe produto
# adicione o produto a lista

# 5 - listagem de produtos:
#  ao escolher a opção 2
# mostre todos os produtos cadastrados
# exiba índice, nome e preço

# 6 - compra produto:
# Ao escolher a opçaõ 3
# Solicite o numero do produto
# solicite a quantidade
# calcule o total a pagar (valor * preço)
# informe se o valor total é menor que 100 -> sem desconto
# utilize expressões relacionais e elogicas

# 7 - tratamento de erros:
# utilize try / except para tratar
# valores inválidos
# índices inexistentes
# entradas não numéricas
# 8 - encerramento:
# ao escolher a opção 4
# exiba uma mensagem de encerramento
# finalize o programa
produtos = []

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def exibir(self):
        print (f' nome: {self.nome} preço: {self.preco}')

def cadastrarProdutos():
    while True:
        try: 
            print("Digite as informações pedidas")
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            produto = Produto(nome, preco)
            return produto
        except(ValueError):
            print("Insira um valor valido, insira novamente")
def listarProdutos():
    if (len(produtos) <= 0):
        print("Nenhum produto foi cadastrado")
    for produto in produtos:
        produto.exibir()
print("Ola cliente, selecione o que deseja fazer no nosso sistema!")
Rodando = True
while Rodando:
    print("Digite 1 para cadastrar produtos")
    print("Digite 2 para listar produtos")
    print("Digite 3 para comprar produtos")
    print("Digite 4 para sair")
    try:
        resposta = int(input("Digite uma das opções: "))
        if (resposta < 1 and resposta > 4):
            raise ValueError
        match resposta:
            case 1:
                while True:
                    produtos.append(cadastrarProdutos())
                    continuar = input("Deseja cadastrar mais algum produto? Digite S se sim e qualquer tecla se não \n")
                    if (continuar != "S"):
                        print("Voltando para o menu")
                        break
            case 2:
                listarProdutos()
                continuar = input("Aperte qualquer tecla pra continuar...")
                break
            case 4:
                print("Finalizando o programa")
                Rodando = False

                

    except(ValueError):
        print("Valor invalido, digite uma das opções mostradas")