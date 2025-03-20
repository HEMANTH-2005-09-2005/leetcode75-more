class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                prev_e=(i==0 or flowerbed[i-1]==0)
                next_e=( i==len(flowerbed)-1 or flowerbed[i+1]==0 )
                if next_e and prev_e :
                    flowerbed[i]=1
                    n-=1
 
        return n<=0
