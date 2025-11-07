from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        # 1) prefix sum of stations to compute base power quickly
        ps = [0] * (n + 1)
        for i, a in enumerate(stations):
            ps[i + 1] = ps[i] + a

        def base_power(i: int) -> int:
            L = max(0, i - r)
            R = min(n - 1, i + r)
            return ps[R + 1] - ps[L]

        base = [base_power(i) for i in range(n)]

        # 2) can(x): can we ensure every city has at least x power with <= k extra stations?
        def can(x: int) -> bool:
            # difference array to "expire" the coverage of extra stations
            diff = [0] * (n + 1)
            cur_add = 0       # total extra power from added stations affecting current city
            remaining = k     # how many stations we can still add

            for i in range(n):
                cur_add += diff[i]  # apply expirations that start at i
                current_power = base[i] + cur_add

                if current_power < x:
                    need = x - current_power
                    if need > remaining:
                        return False
                    remaining -= need

                    # place 'need' new stations as far right as possible: at pos = min(n-1, i + r)
                    pos = min(n - 1, i + r)
                    # those stations contribute immediately to city i and up to (pos + r)
                    cur_add += need
                    end = pos + r + 1
                    if end <= n:
                        diff[end] -= need  # their effect stops after index (pos + r)

            return True

        # 3) Binary search for the maximum minimal power
        lo = min(base)
        hi = max(base) + k  # upper bound: dump all extras into the best place

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo