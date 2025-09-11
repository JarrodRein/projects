class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        extracted = sorted([c for c in s if c in vowels])
        j = 0
        result =[]