#a shorter version of the above code and same logic (but pythonic)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]
