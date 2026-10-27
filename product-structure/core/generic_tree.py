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
        
        
    def remover(self, node:Node):
        if node is None:
            return None

        if node.id in self.nodes:
            self.nodes.pop(node.id)

            for n in node.children:
                self.remover(n)

    def alterar(self, node, new_value):
        if node is None:
            return None

        if node.id in self.nodes:
            self.nodes[node.id].value = new_value

    def exibir(self):
        pass