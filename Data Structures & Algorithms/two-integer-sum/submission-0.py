class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for idx, num in enumerate(nums):
            hashMap[num] = idx
        
        for idx,num in enumerate(nums):
            dif = target - num
            if dif in hashMap:
                if hashMap[dif] != idx:
                    return [idx, hashMap[dif]]
        