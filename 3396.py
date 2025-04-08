from typing import List
class Solution:

    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        def is_distinct(arr):
            if not arr:  
                return True
            seen = set()
            for num in arr:
                if num in seen:
                    return False
                seen.add(num)
            return True
            
        if is_distinct(nums):
            return 0
            
        if len(nums) <= 3:
            return 1
            
        operations = 0
        remaining = nums[:]
        
        while remaining:
            if is_distinct(remaining):
                return operations
                
            elements_to_remove = min(3, len(remaining))
            remaining = remaining[elements_to_remove:]
            operations += 1
            
        return operations