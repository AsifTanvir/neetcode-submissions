class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        # for val in strs:
        #    valSorted = "".join(sorted(val))
        #    result[valSorted].append(val)
        for val in strs:
            charCount = [0]*26
            # charCount = 0
            for char in val:
                charCount[ord(char) - ord('a')] += 1
            result[tuple(charCount)].append(val)
            # print(result)
        return list(result.values())

        