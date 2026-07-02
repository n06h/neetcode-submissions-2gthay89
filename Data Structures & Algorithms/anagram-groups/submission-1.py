class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap
        seen = {}
        #key
        for i in strs:
            letters = [0]*26
            for j in i:
                letters[ord(j)-ord("a")] += 1
            key = tuple(letters)
            if key in seen:
                seen[key].append(i)
            else:
                seen[key] = [i]
        return list(seen.values())
        