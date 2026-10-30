from product_structure.core.node import Node


class ArvoreFormula:
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
            print("Pai inexistente.")

        return None

    def remover(self, node: Node):
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

    def buscar_por_id(self, search_id: int) -> Node | None:
        return self.nodes.get(search_id)

    def buscar_por_nome(self, name: str) -> dict[int, Node]:
        resultado = {}

        for node in self.nodes:
            if node.value.nome == name:
                resultado[node.node_id] = node

        return resultado

    def exibir(self):
        pass
