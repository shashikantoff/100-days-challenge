class Solution:
    def minEatingSpeed(self, piles, h):
        start = 1
        end = max(piles)
        ans = end

        while start <= end:
            mid = start + (end - start) // 2

            if self.isPossible(piles, mid, h):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return ans

    def isPossible(self, piles, speed, h):
        hours = 0
        for p in piles:
            hours += p // speed
            if p % speed > 0:
                hours += 1
        
        return hours <= h
