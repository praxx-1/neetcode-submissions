class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans=set()


        for i in range(len(nums)):
            target= -nums[i]
            l=i+1
            r=len(nums)-1
            
            while l < r :
                if nums[l] + nums[r] == target :
                    ans.add(tuple(sorted([nums[i],nums[l],nums[r]])))
                    l+=1

                elif nums[l] + nums[r] > target :
                    r-=1
                else:
                    l+=1
        return [list(x) for x in ans]

