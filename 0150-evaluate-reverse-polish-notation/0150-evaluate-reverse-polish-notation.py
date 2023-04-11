class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i =="+":
                stack.append(stack.pop()+stack.pop())
            elif i=="-":
                num2=stack.pop()
                num1=stack.pop()
                stack.append(num1-num2)
            elif i=="*":
                stack.append(stack.pop()*stack.pop())
            elif i=="/":
                num2=stack.pop()
                num1=stack.pop()
                stack.append(int(num1/num2))
            else:
                stack.append(int(i))
                             
        return stack.pop()
            
        