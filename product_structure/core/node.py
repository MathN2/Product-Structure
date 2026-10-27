class Node:
    def __init__(self, value, id):
        self.value = value
        self.id = id
        self.tree_id = None
        self.parent_id = None
        self.children = []
        self.depth = 0