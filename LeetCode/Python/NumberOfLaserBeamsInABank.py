class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        banks = [row.count('1') for row in bank if '1' in row]
        return sum(banks[i] * banks[i - 1] for i in range(1, len(banks)))   