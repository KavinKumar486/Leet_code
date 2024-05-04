class Solution(object):
    def numSubarraysWithSum(self, nums, x):
        
        def hel(x):
            if x < 0:
                return 0
            l, cur = 0, 0
            res = 0  # Initialize res here
            for r in range(len(nums)):
                cur += nums[r]
                while cur > x:
                    cur -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res
        
        return hel(x) - hel(x - 1)
