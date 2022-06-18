# Currently under development, so this is for debug purposes
from pygraphv import node

class PrefixTreeNode(node.Node):
    def __init__(self, value: str):
        super().__init__(value)
        self.value = value
        self.node_children = {}

    @staticmethod
    def construct_tree(words: list[str]):
        tree = PrefixTreeNode(" ")
        for word in words:
            curr = tree
            for char in word:
                if char not in curr.node_children:
                    curr.node_children[char] = PrefixTreeNode(char)
                    curr.children.append(curr.node_children[char])
                curr = curr.node_children[char]

        return tree