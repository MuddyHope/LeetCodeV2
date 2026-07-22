class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        r = Counter(ransomNote)
        m = Counter(magazine)
    
        for letter in ransomNote:
            if not m.get(letter, 0):
                return False
            m[letter] = m.get(letter) -1
            if m.get(letter) == 0:
                del m[letter]
        return True
