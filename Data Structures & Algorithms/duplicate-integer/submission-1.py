class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """Plan: 
        naive method, iterate through the list, store unique numbers in
        a seperate list and check if the current number is in the list.
        would be o(n**2), as iterating through two arrays

        Optimal solution: store numbers in a hash map, if two numbers have the
        same key, output false

        """
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        
    