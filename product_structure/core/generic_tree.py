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
            self.nodes[node.node_id] = node
            return node
        
        if parent.node_id in self.nodes:
            parent.children.append(node)
            node.parent = parent
            self.nodes[node.node_id] = node
            return node

        else:
            print('Pai inexistente.')

        return None
        
        
    def remover(self, node:Node):
        if node is None:
            return

        if node.node_id in self.nodes:
            self.nodes.pop(node.node_id)

            for n in node.children:
                self.remover(n)


    def alterar(self, node, new_value):
        if node is None:
            return

        if node.node_id in self.nodes:
            self.nodes[node.node_id].value = new_value


    def exibir(self):
        pass

a = Arvore()

n1 = Node(1, 1)
n2 = Node(2, 2)
n3 = Node(3, 3)
n4 = Node(4, 4)
n5 = Node(5, 5)
a.inserir(n1)
a.inserir(n2, n1)
a.inserir(n3, n2)
a.inserir(n4, n1)
a.inserir(n5, n4)
a.remover(n2)
a.alterar(n4, 8)

print([node.node_id for node in a.nodes.values()])
print([node.value for node in a.nodes.values()])