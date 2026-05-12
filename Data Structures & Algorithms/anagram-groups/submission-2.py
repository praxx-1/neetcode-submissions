class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ana={}

        for word in strs :
            key=tuple(sorted(word))

            if key not in ana :
                ana[key]=[word]
            else:
                ana[key].append(word)
        return list(ana.values())
        """
        
        ana={}

        for word in strs :
            count=26*[0]

            for letter in word :
                count[ord(letter)-97]+=1
            
            count=tuple(count)
            
            if count not in ana:
                ana[count]=[word]
            else:
                ana[count].append(word)
        return list(ana.values())



                
