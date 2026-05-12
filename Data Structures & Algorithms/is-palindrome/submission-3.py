class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new=""
        for x in s:
            if x.isalpha() or x.isdigit():
                new+=x
        
        l=0
        r=len(new)-1

        while l < r :
            if new[l] != new[r] :
                return False
            l+=1
            r-=1
            
        return True