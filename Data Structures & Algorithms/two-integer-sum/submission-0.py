class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        we can store the difference in a hash map, than check if j 
        is in the hash map.
        """
        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference],i]
            else:
                seen[nums[i]] = i


            
            

