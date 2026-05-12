class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force solution
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j :
                    return [i,j]
        """
        #optimised solution
        seen={}
        for i, n in enumerate(nums):
            seen[n] = i
                

        for i,n in enumerate(nums):
            diff=target-n
            if diff in seen and seen[diff] != i :
                return [i,seen[diff]]
        return []   


