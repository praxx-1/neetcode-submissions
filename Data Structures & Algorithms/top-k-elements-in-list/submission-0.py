class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        counter = []
        ans = []

        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1

        for key, value in count.items():
            counter.append([key, value])

        counter.sort(key=lambda x: x[1], reverse=True)

        for i in range(k):
            ans.append(counter[i][0])

        return ans
