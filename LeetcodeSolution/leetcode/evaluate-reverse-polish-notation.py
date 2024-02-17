class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if  token=="+":
                first=stack.pop()
                second=stack.pop()
                stack.append(first+second)
            elif token=="-":
                second=stack.pop()
                first=stack.pop()
                stack.append(first-second)
            elif token=="*":
                first=stack.pop()
                second=stack.pop()
                stack.append(first*second)
            elif token=="/":
                second=stack.pop()
                first=stack.pop()
                if (first>0 and second>0) or (first<0 and second<0):
                    stack.append(first//second)
                elif second!=0:
                    first=abs(first)
                    second=abs(second)
                    div=-(first//second)
                    stack.append(div)
                
            else:
                stack.append(int(token))
        return stack[0]