from .words import MIN_WORDS
from .prefix_tree import PrefixTreeNode

class AutoComplete:
    def __init__(self, words=MIN_WORDS):
        self.tree = PrefixTreeNode.construct_tree(words)

    def _get_completion_of_node(self, node: PrefixTreeNode):
        res = []
        if node.is_word:
            res.append(node.value)
        for i in node.children.values():
            res.extend(self._get_completion_of_node(i))

        return res

    def get_completions(self, word: str):
        curr = self.tree
        for char in word:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        return self._get_completion_of_node(curr)