class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        signSet={"+","-","*","/"}
        for element in tokens:
            if element in signSet:
                if element == "+":
                    sum = stack.pop()+stack.pop()
                    stack.append(sum)
                elif element == "-":
                    difference= -(stack.pop()-stack.pop())
                    stack.append(difference)
                elif element == "*":
                    product=stack.pop()*stack.pop()
                    stack.append(product)
                else:
                    denominator=stack.pop()
                    numerator=stack.pop()
                    stack.append(numerator/denominator)
            else:
                stack.append(int(element))
            print(stack)
        print("\n")
        return stack[0]
    

solution = Solution()
tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
result = solution.evalRPN(tokens)