class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        tar_x=target[0]
        tar_y=target[1]
        for x,y in ghosts:
            all_unit=abs(tar_x)+abs(tar_y)
            step=abs(tar_x-x)+abs(tar_y-y)
            if (x,y)==(tar_x,tar_y):
                return False
            if step<=all_unit:
                return False
        return True
            
            
            