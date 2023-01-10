from typing import List

from .words import MIN_WORDS
from .prefix_tree import PrefixTreeNode

class AutoComplete:
    """
    Main class in pyauto-compl library
    Used for finding completions of words
    """
    def __init__(self, words: List[str] = MIN_WORDS):
        self.tree = PrefixTreeNode.construct_tree(words)

    def _get_completions_of_node(self, node: PrefixTreeNode) -> List[str]:
        """
        Gets all completion of a node
        Uses recursion, be careful
        """
        res = []
        if node.is_word:
            res.append(node.value)
        for i in node.children.values():
            res.extend(self._get_completions_of_node(i))

        return res

    def get_completions(self, word: str) -> List[str]:
        """
        Gets all completions of a word
        """
        curr = self.tree
        for char in word:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        return self._get_completions_of_node(curr)