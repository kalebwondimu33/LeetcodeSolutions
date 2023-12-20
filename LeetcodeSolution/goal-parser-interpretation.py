class Solution:
    def interpret(self, command: str) -> str:
        stack=[]
        ans=""
        for i in range(len(command)):
            if  command[i]=="(":
                stack.append(command[i])
            elif command[i]=="G":
                ans+="G"
            elif command[i]==")" and stack[-1]=="(":
                ans+="o"
            elif command[i]==")" and stack[-1]=="l":
                ans+="al"
            else:
                stack.append(command[i])
                
        return ans
        