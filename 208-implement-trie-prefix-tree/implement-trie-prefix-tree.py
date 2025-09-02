class Node:
    def __init__(self, val: str|None = None, next={}):
        self.val = None
        self.next = {}
        self.is_end = False 

class Trie:

    def __init__(self):
        # create a rootNode with No value
        self.root_node = Node("*", next={})

        
    def insert(self, word: str) -> None:            
        # start with insert new word only
        # print(f"inserting: {word}")
        curr = self.root_node
        for letter in word:
            if letter not in curr.next.keys():
                curr.next[letter] = Node(letter)
            # print(f"curr.next is {curr.next}")
            curr = curr.next[letter]
        curr.is_end = True


    def search(self, word: str) -> bool:
        curr = self.root_node
        i = 0
        # print(f"searching word: {word}")
        while curr and i <= len(word) - 1:
            if word[i] in curr.next:
                # print(f"i: {i}, letter: {word[i]} present in curr.next: {curr.next}")
                curr = curr.next[word[i]]
                i += 1
            else:
                # print(f"not found, i: {i}, letter: {word[i]} in curr.next: {curr.next}")
                return False
        return curr.is_end

            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root_node
        i = 0
        # print(f"prefix : {prefix}")
        while i <= len(prefix) - 1:
            if prefix[i] in curr.next:
                # print(f"startswith i: {i}, letter: {prefix[i]} present in curr.next: {curr.next}")
                curr = curr.next[prefix[i]]
                i += 1
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)