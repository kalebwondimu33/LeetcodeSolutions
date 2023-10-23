class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        count=0
        if len(password)<8:
            return False
        m=t=w=tt=f=False
        for i in password:
            if i.isupper():
                m=True
            if i.islower():
                t=True
            if i.isdigit():
                w=True
            if i in "!@#$%^&*()-+":
                tt=True
        for i in range(1,len(password)):
            if password[i-1]==password[i]:
                return False
        f=True
        if  m==True and t==True and w==True and tt==True and f==True:
            return True
        else:
            return False
            
                
            
        