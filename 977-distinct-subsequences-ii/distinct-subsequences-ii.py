class Solution:
    def distinctSubseqII(self, s):
        mod = 10**9 + 7
        dp = 1
        last = {}

        for c in s:
            new = dp * 2
            if c in last:
                new -= last[c]

            last[c] = dp
            dp = new % mod

        return (dp - 1) % mod