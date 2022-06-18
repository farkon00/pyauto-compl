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
            curr_word = ""
            for char in word:
                curr_word += char
                if char not in curr.node_children:
                    curr.node_children[char] = PrefixTreeNode(curr_word)
                    curr.children.append(curr.node_children[char])
                curr = curr.node_children[char]

        return tree