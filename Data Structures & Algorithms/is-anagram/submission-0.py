class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        sort them in alphabetical order, than add to a hash map and
        check if they contain the same key
        """
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        if s == t:
            return True
        else:
            return False