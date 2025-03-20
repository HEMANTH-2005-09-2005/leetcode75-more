class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x=max(candies)
        res=[]
        for c in candies:
            if c+extraCandies >= x:
                res.append(True)
            else:
                res.append(False)
        
        return res
