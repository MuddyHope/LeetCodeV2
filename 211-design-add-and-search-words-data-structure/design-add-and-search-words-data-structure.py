class Node:

    def __init__(self, val, next={}):
        self.val = val
        self.next = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        # intitalise the root
        self.root = Node("*", next={})
        

    def addWord(self, word: str) -> None:
        i = 0
        curr = self.root
        my_set = set()
        while i<len(word) and curr:
            if word[i] not in curr.next:
                curr.next[word[i]] = Node(word[i])
            curr = curr.next[word[i]]
            i += 1
        curr.is_end = True


    def search(self, word: str) -> bool:
        def backtrack(node, i):

            # ✅ if we've consumed the word, check if this node is an end
            if i == len(word):
                return node.is_end

            ch = word[i]

            # ✅ handle wildcard
            if ch == ".":
                for child in node.next.values():
                    if backtrack(child, i + 1):
                        return True
                return False
            else:
                if ch not in node.next:
                    return False
                return backtrack(node.next[ch], i + 1)

        return backtrack(self.root, 0)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)