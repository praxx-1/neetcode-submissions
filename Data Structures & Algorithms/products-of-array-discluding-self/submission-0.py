class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=[]

        pref = [1] * n
        suff = [1] * n

        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]

        for i in range(len(nums)):
            ans.append(suff[i]*pref[i])
        return ans