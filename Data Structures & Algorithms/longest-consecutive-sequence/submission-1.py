class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using sorting method
        if not nums:
            return 0
        
        nums.sort()
        longestVal = 0
        result = 0
        idx = 0
        currVal = nums[idx]

        while idx < len(nums):
            if currVal != nums[idx]:
                currVal = nums[idx]
                longestVal = 0
                # idx += 1
                # To skip any repeating number
            while idx < len(nums) and currVal == nums[idx]:
                idx += 1
                
            currVal += 1
            longestVal += 1
            
            result = max(result, longestVal)
        return result