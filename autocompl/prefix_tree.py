from typing import List

class PrefixTreeNode:
    """
    Node of prefix tree, data structure used by pyauto-compl to store words
    """
    def __init__(self, value: str):
        self.value = value
        self.is_word = False
        self.children = {}

    @classmethod
    def construct_tree(cls, words: List[str]):
        """
        Constructs prefix tree from list of words
        """
        tree = cls(" ")
        for word in words:
            curr = tree
            curr_word = ""
            for char in word:
                curr_word += char
                if char not in curr.children:
                    curr.children[char] = cls(curr_word)
                curr = curr.children[char]
            curr.is_word = True

        return tree