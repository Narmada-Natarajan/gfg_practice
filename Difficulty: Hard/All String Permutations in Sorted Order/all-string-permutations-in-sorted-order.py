from itertools import permutations

class Solution:
    def permutation(self, s):
        ans = permutations(s)

        res = []

        for p in ans:
            res.append("".join(p))

        return sorted(res)