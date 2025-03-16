class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict = {}
        if(len(s) != len(t)): return False
        for i in s:
            if i not in mydict:
                mydict[i] = 1
            elif i in mydict:
                mydict[i] +=1
         
        for j in t:
            if j in mydict:
                mydict[j] -= 1   
        res = not any(mydict.values())
        return res
       
        