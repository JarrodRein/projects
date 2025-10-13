class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]  # start with the first word
        
        for word in words[1:]:
            # Compare sorted versions of last kept word and current
            if sorted(word) != sorted(res[-1]):
                res.append(word)
                
        return res