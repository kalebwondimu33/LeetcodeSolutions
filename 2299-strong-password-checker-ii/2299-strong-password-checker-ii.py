class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        count=0
        if len(password)<8:
            return False
        m=t=w=tt=False
        for i in range(len(password)) :
            if password[i].isupper():
                m=True
            if password[i].islower():
                t=True
            if password[i].isdigit():
                w=True
            if password[i] in "!@#$%^&*()-+":
                tt=True
            if i!=len(password)-1 and password[i]==password[i+1]:
                return False
        return m and t and w and tt 
            
       
            
                
            
        