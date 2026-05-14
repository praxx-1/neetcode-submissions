class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        low=nums[0]

        while i <= j :
            low=min(low,nums[i],nums[j])
            i+=1
            j-=1
        return low