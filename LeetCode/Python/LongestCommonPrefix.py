class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current = ""
        
        for i in range(min(len(s) for s in strs)): # find the shortest string length
            if not strs:  # handle empty list case
                return current  
            current_char = strs[0][i] # take the character from the first string
            # check if all strings have the same character at position i
            for s in strs: # check each string
                if s[i] != current_char: # if any string differs, return current
                    return current # if we reach here, all strings have the same character at position i
            current += current_char # append the character to the current prefix
        return current # if we finish the loop, all characters matched up to the shortest string length
        # return the accumulated prefix