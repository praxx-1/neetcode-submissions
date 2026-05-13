class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count=0
        prev=0

        ult=[]
        n=len(position)



        for i in range(n):
            ult.append([position[i],speed[i]])


        ult.sort(key=lambda x : x[0] , reverse = True )

        for pos,speed in ult:
            
            currtime = (target - pos ) / speed

            
            if currtime > prev :
                count+=1
                prev=currtime
            
        
        return count
