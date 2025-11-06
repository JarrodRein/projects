from collections import Counter
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []

        # Frequency of the first window
        freq = Counter(nums[:k])

        def window_xsum(freq_map: Counter) -> int:
            # Build (freq, value) pairs and sort
            items = [(cnt, val) for val, cnt in freq_map.items()]
            items.sort(key=lambda t: (-t[0], -t[1]))  # by freq desc, then value desc

            total = 0
            take = x
            for cnt, val in items:
                if take == 0:
                    break
                total += val * cnt
                take -= 1
            return total

        # x-sum for the first window
        ans.append(window_xsum(freq))

        # Slide the window
        for i in range(k, n):
            out_val = nums[i - k]
            in_val = nums[i]

            # remove outgoing
            freq[out_val] -= 1
            if freq[out_val] == 0:
                del freq[out_val]

            # add incoming
            freq[in_val] += 1

            ans.append(window_xsum(freq))

        return ans