class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        count1=26 * [0]

        for x in s1 :
            count1[ord(x)-97]+=1




        l = 0
        r =  len(s1) 


        while r < len(s2) + 1:

            window=s2[l:r]
            
            count2 = 26 * [0]
            
            for x in window :
                count2[ord(x)-97]+=1
                

            
            if count1 == count2 :
                return True
                
            l+=1
            r+=1
        else:
            return False

        """
        l1=len(s1)
        l2=len(s2)

        if l1 > l2 :
            return False

        count1 = 26 * [0]
        count2 = 26 * [0]

        for i in range(l1) :
            
            count1[ord(s1[i])-97]+=1
            count2[ord(s2[i])-97]+=1

        if count1 == count2:
            return True
        for i in range(l1,l2):
            count2[ord(s2[i])-97 ] += 1
            count2[ord(s2[i - l1])- 97]-= 1
            if count1 == count2:
                return True

        return False


