from product_structure.core.generic_tree import ArvoreFormula
from product_structure.core.node import Node


def explosao(produto: ArvoreFormula):
    if produto.root is None:
        return

    root = produto.root

    resultado = {
        "nome": root.value.nome,
        "preco": produto.implosao(),
        "componentes": [],
    }

    for child in root.children:
        resultado["componentes"].append(formatacao(child))

    return resultado


def formatacao(node: Node):
    r = {
        "nome": node.value.nome,
        "quantidade": node.value.quantidade,
        "preco": node.value.preco,
        "componentes": [],
    }

    for child in node.children:
        r["componentes"].append(formatacao(child))

    return r
