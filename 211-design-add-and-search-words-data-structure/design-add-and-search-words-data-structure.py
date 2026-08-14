class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()

            curr = curr.children[letter]

        curr.isWord = True

    def search(self, word: str) -> bool:

        def dfs(node, i):

            # We consumed the entire search word
            if i == len(word):
                return node.isWord

            letter = word[i]

            # Normal character
            if letter != ".":
                if letter not in node.children:
                    return False

                return dfs(node.children[letter], i + 1)

            # "." means any character
            for child in node.children.values():
                if dfs(child, i + 1):
                    return True

            return False

        return dfs(self.root, 0)