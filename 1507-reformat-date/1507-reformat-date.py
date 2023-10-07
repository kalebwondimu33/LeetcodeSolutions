class Solution:
    def reformatDate(self, date: str) -> str:
        month= {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        dates=date.split()
        output=""
        output+=dates[-1]
        output+="-"
        output+=month[dates[-2]]
        output+="-"
        num=dates[0][:2]
        if num[-1].isnumeric():
            output+=num
        else:
            output+=f"0{num[0]}"
        return output
        
        
        
        
        