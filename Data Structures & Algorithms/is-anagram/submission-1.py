class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else: 
            array = [0]*26
            for i in range(len(s)):
                array[ord(s[i])-ord("a")] +=1
                array[ord(t[i])-ord("a")] -=1
            for i in array:
                if i != 0:
                    return False
            return True
                