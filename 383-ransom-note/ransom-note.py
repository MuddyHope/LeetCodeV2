class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        r_counter = dict(Counter(ransomNote))
        m_counter = dict(Counter(magazine))

        for k,v in r_counter.items():
            if v > m_counter.get(k, 0):
                return False
        return True

