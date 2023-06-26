class Solution:
    def minTimeToType(self, word: str) -> int:
        count=0
        dic={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        j=0
        for i in word:
            temp=abs(abs(dic[i]-j)-26)+1
            temp1=(abs(dic[i]-j))+1
            print(temp)
            print(temp1)
            if temp>temp1:
                count+=temp1
            else:
                count+=temp
            j=dic[i]
        return count
            
            
            
        