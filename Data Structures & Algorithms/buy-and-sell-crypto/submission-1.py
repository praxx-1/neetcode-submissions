class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l=0
        r= l+1

        ans=0

        while r < len(prices) :
            sale = prices[r] - prices[l]
            
            if prices[r] < prices[l] :
                l+=1
                r=l+1
            else:
                r = r+1
            ans=max(ans,sale)
        return ans