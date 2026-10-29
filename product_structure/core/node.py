from dataclasses import dataclass, field


@dataclass
class Node[T]:
        node_id: int
        value: T
        tree_id: int | None = None
        parent: Node[T] | None = None
        children: list[Node[T]] = field(default_factory=list)
        depth: int = 0