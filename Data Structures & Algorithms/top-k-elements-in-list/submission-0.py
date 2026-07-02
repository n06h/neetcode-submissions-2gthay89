class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count how many times each number appears
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
            
        # Step 2: Group the numbers by their frequency
        # (Must be defaultdict(list) so we can append numbers to it!)
        buckets = defaultdict(list)
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Step 3: Harvest the top k elements by counting down from max frequency
        result = []
        for freq in range(len(nums), 0, -1):
            if freq in buckets:
                for num in buckets[freq]:
                    result.append(num)
                    
                    # If we've gathered exactly k elements, we are DONE!
                    if len(result) == k:
                        return result
                        
        return result