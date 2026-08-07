class Produto:
    def __init__(self, codigo, nome, qnt ,precoUni):
        self.codigo = codigo
        self.nome = nome
        self.qnt = qnt
        self.precoUni = precoUni
        self.preco = qnt * precoUni
    def mostrar(self):
        print(f"seu codigo: {self.codigo}, nome: {self.nome}, quantidade: {self.qnt}, preço unitario: {self.precoUni}, o preço total foi de: {self.preco}")

produto = Produto(15, "Console", 5, 4000.00)
produto.mostrar()