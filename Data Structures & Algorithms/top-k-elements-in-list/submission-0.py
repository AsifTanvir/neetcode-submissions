class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for num in nums:
            numCount[num] = 1 + numCount.get(num,0)
        
        res = []
        for number, count in numCount.items():
            res.append([count, number])
            # print(res)
        res.sort()
        # print(res)

        finalRes = []
        while len(finalRes) < k:
            finalRes.append(res.pop()[1])
        
        return finalRes
