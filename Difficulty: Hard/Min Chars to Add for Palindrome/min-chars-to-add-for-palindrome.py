class Solution:
    def minChar(self, s):
        
        if not s:
            return 0

        comb = s + '$' + s[::-1]
        n = len(comb)

        # Build the tracking array (LPS table)
        lps = [0] * n
        j = 0 

        for i in range(1, n):
            # If characters don't match, jump back using the lps table
            while j > 0 and comb[i] != comb[j]:
                j = lps[j - 1]

            # If characters match, move our match pointer forward
            if comb[i] == comb[j]:
                j += 1

            lps[i] = j

        # Answer is just: total length minus the last value in our table
        return len(s) - lps[-1]
        
        