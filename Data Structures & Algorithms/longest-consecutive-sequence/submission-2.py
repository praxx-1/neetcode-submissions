class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums :
            return 0 
            
        seq=1
        high=1
        nums.sort()
        
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            elif nums[i] - nums[i-1] == 1:
                seq+=1
            else:
                seq=1
            high=max(high,seq)

        return high