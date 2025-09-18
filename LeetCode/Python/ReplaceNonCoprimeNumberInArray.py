class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            cur = x
            # Keep merging with the stack top while non-coprime
            while st:
                g = gcd(st[-1], cur)
                if g == 1:
                    break
                cur = (st[-1] // g) * cur   # LCM(st[-1], cur) but avoiding overflow
                st.pop()
            st.append(cur)
        return st