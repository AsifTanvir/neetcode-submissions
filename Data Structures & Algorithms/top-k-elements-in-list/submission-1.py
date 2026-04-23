class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for num in nums:
            numCount[num] = 1 + numCount.get(num,0)
        
        ## Using The Sorting method
        # res = []
        # for number, count in numCount.items():
        #     res.append([count, number])
        #     # print(res)
        # res.sort()
        # # print(res)

        # finalRes = []
        # while len(finalRes) < k:
        #     finalRes.append(res.pop()[1])
        
        # return finalRes

        ## Using bucket sort
        # freqArr = [[] for i in range(len(nums) + 1)]
        freqArr = {}
        for i in range(len(nums)+1):
            freqArr[i] = []
        # print(freqArr)
        for number, count in numCount.items():
            freqArr[count].append(number)
        # print(freqArr)

        res = []
        for key in reversed(list(freqArr.keys())):
            val = freqArr[key]
            for num in val:
                res.append(num)
                if len(res) == k:
                    return res

