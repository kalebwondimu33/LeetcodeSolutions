class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if mainTank<5:
            return mainTank*10
        distance=0
        while mainTank>=5:
            distance+=5*10
            if additionalTank>=1:
                mainTank-=4
                additionalTank-=1
            else:
                mainTank-=5
        distance+=mainTank*10
        return distance