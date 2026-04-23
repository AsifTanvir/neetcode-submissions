class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        nums.sort() ## there goes O(nlogn)

        for i, num in enumerate(nums):
            if num > 0:
                # in the sorted array, if the first index is not negative or 0,
                # you can not get a summation of 0
                break
            # skipping duplicates
            if i>0 and num == nums[i-1]:
                continue
            target = - num
            left = i+1
            right = length - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    ## If there are duplicates between left and right indices, skip them
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return result        
            