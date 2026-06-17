class Solution:
    def myAtoi(self, s: str) -> int:
        
        res = []
        sign = 0    # 0-> +ve, 1 -> -ve
        digits_found = False
        sign_found = False
        

        # find from where digits are found and also check if its positive or not
        if not s:
            return 0
        for i in range(len(s)):
            if s[i] == " " and not sign_found and not digits_found:
                continue
            elif s[i] == "-" and not sign_found:
                sign = 1
                sign_found = True
            elif s[i] == "+" and not sign_found:
                sign_found = True
                sign = 0
            else:
                digits_found = True
                break
        
        start = i

        while start < len(s):
            if 65 <= ord(s[start]) <= 90 or 97 <= ord(s[start]) <= 122 or s[start] in ("+", "-", ".", " "):
                # check lowercase character
                break
            elif 0 <= int(s[start]) <= 9:
                res.append(int(s[start]))
            
            start += 1
        
        i = 1
        output = 0
        for each in reversed(res):
            output += each * i
            i *= 10

        if sign == 1:
            output *= -1

        if output < -2147483648:
            return -2147483648

        if output > 2147483647:
            return 2147483647

        return output

