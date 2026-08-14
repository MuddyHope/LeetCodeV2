class Trie:
    def __init__(self, val=0):
        self.val = val
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Trie(letter)

            curr = curr.children[letter]

        curr.is_word = True

    def search(self, word: str) -> bool:

        stack = [(self.root, 0)]

        while stack:

            curr, i = stack.pop()

            # We consumed the entire word
            if i == len(word):
                if curr.is_word:
                    return True
                continue

            # Wildcard
            if word[i] == ".":
                for child in curr.children.values():
                    stack.append((child, i + 1))

            # Normal character
            else:
                if word[i] in curr.children:
                    child = curr.children[word[i]]
                    stack.append((child, i + 1))

        return False