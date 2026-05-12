class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count=26*[0]

        for x in s:
            count[ord(x)-97]+=1
        
        for x in t:
            count[ord(x)-97]-=1
        
        for x in count :
            if x >= 1 or x <= -1 :
                return False
        return True