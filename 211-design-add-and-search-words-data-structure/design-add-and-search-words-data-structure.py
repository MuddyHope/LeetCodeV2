class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Trie()
            curr = curr.children[letter]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        def dfs(i, curr):
            # print(f"curr_children: {curr.children}")
            if i == len(word):
                return curr.is_word
            
            if word[i] == "." and word[i] not in curr.children:
                for children in curr.children.values():
                    if dfs(i+1, children):
                        return True
                return False
            
            else: 
                if word[i] in curr.children:
                    return dfs(i+1, curr.children[word[i]])
                return False


        return dfs(0, curr)
    

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)