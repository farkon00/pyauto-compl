from typing import List

class PrefixTreeNode:
    """
    Node of prefix tree, data structure used by pyauto-compl to store words
    """
    def __init__(self, value: str):
        self.value = value
        self.is_word = False
        self.children = {}

    @staticmethod
    def construct_tree(words: List[str]):
        """
        Constructs prefix tree from list of words
        """
        tree = PrefixTreeNode(" ")
        for word in words:
            curr = tree
            curr_word = ""
            for char in word:
                curr_word += char
                if char not in curr.children:
                    curr.children[char] = PrefixTreeNode(curr_word)
                curr = curr.children[char]
            curr.is_word = True

        return tree