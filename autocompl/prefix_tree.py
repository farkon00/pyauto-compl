class PrefixTreeNode:
    def __init__(self, value: str):
        self.value = value
        self.is_word = False
        self.children = {}

    @staticmethod
    def construct_tree(words: list[str]):
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