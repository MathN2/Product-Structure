from node import Node

class Arvore:
    def __init__(self):
        self.root = None
        self.nodes = {}

    def inserir(self, node, parent=None):
        if node is None:
            return None

        if parent is None:
            self.root = node
            self.nodes[node.id] = node
            return node
        
        if parent.id in self.nodes:
            parent.children.append(node)
            node.parent_id = parent.id
            self.nodes[node.id] = node
            return node

        else:
            print('Pai inexistente.')

        return None
        
        
    def remover(self, node):
        pass

    def alterar(self, new_value):
        pass

    def exibir(self):
        pass


a = Arvore()

n1 = Node(0, 1)
n2 = Node(0, 2)
a.inserir(n1)
a.inserir(n2, n1)

print(a.nodes)