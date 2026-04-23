class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        # mult = 1
        # zero_count = 0
        # for val in nums:
        #     if val == 0:
        #         zero_count += 1
        #     else:
        #         mult *= val
        
        # if zero_count > 1: return [0]*len(nums)

        # for idx, val in enumerate(nums):
        #     if zero_count > 0:
        #         if val == 0: res[idx] = mult
        #         else: res[idx] = 0
        #     else:
        #         res[idx] = mult//val
        
        # Without using division
        prefix = 1
        postfix = 1
        start = 0
        end = len(nums) - 1
        for val in nums:
            res[start] = prefix
            prefix *= val
            start += 1

        for idx in range(end, -1, -1):
            res[idx] *= postfix
            postfix *= nums[idx]
        
        return res