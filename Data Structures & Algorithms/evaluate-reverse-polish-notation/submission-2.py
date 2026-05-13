class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        exp={'+', '-', '*', '/'}


        for x in tokens:
            if x in exp :
                b=stack.pop()
                a=stack.pop()

                if x == "+" :
                    stack.append(a+b)
                elif x == "-" :
                    stack.append(a-b)
                elif x == "*" :
                    stack.append(a*b)
                else: 
                    stack.append(int(a/b))

            else:
                stack.append(int(x))
        return stack[-1]


        