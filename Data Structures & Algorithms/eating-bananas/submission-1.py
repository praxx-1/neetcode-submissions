class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l=1
        r= max(piles)

        def calculate(arr,val):
            count=0
            for x in piles :
                count+=(x + val - 1) // val
            return count
                
        ans=0
        while l <= r :
            
            mid = (l+r)//2
            
            
            if calculate(piles,mid) <= h :
                ans = mid
                r = mid -1
            else:
                l = mid +1
        return ans

