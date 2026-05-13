class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opeaning={"(","{","["}
        closing={")","}","]"}
        

        for x in s :

            if x in opeaning :
                stack.append(x)

            elif x in closing :
                if not stack :
                    return False
                if x == ")" and stack[-1] == "(" :
                    stack.pop()
                elif x == "}" and stack[-1] == "{" :
                    stack.pop()
                elif x == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                return False

        if not stack :
            return True
        else:
            return False
