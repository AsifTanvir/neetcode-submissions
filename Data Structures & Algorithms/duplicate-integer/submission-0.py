class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadySeen = set()
        for num in nums:
            if num in alreadySeen:
                return True
            alreadySeen.add(num)
        return False