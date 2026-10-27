class Node:
    def __init__(self, valor, id):
        self.valor = valor
        self.id = id
        self.tree_id = None
        self.parent_id = None
        self.children = []
        self.depth = 0