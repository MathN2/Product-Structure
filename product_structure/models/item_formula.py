class ItemFormula:
    def __init__(self, nome, quantidade, preco=0):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def atualizar_quantidade(self, new_qtd):
        if new_qtd >= 0:
            self.quantidade = new_qtd

    def atualizar_preco(self, new_price):
        if new_price >= 0:
            self.preco = new_price
