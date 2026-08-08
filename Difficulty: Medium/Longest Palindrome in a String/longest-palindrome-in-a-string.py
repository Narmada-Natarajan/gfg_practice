class Solution:
    def longestPalindrome(self, s):
        t = "^#" + "#".join(s) + "#$"
        p = [0] * len(t)

        center = right = 0
        max_len = 0
        max_center = 0

        for i in range(1, len(t) - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            while t[i + (1 + p[i])] == t[i - (1 + p[i])]:
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

            if p[i] > max_len:
                max_len = p[i]
                max_center = i

        start = (max_center - max_len) // 2
        return s[start:start + max_len]