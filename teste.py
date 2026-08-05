class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco        
    def mostrar (self):
        print(f'produto {self.nome} preco {self.preco}')
p1 = Produto('mouse', 50)
p1.mostrar()