class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        import bisect
        
        n = len(stations)
        
        # build the initial window power via prefix sum
        ps = [0]*(n+1)
        for i in range(n):
            ps[i+1] = ps[i]+stations[i]
        
        def power(i):
            L = max(0, i-r)
            R = min(n-1, i+r)
            return ps[R+1] - ps[L]
        
        # check function: can we make every city ≥ x using ≤ k builds?
        def can(x):
            add = 0
            need = 0
            extra = [0]*(n+1)
            cur = 0
            for i in range(n):
                cur += extra[i]
                val = power(i) + cur
                if val < x:
                    req = x-val
                    need += req
                    if need > k: return False
                    extra_min = min(n-1, i+r)
                    extra[extra_min] += req
                    cur += req
            return True
        
        lo, hi = 0, 10**18
        while lo<hi:
            mid = (lo+hi+1)//2
            if can(mid): lo=mid
            else: hi=mid-1
        return lo