from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        a = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        n = len(a)
        starts = [x[0] for x in a]

        nxt = [
            bisect_right(starts, a[i][1])
            for i in range(n)
        ]

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, idx = a[i]

            for k in range(1, 5):
                skip = dp[i + 1][k]

                score = w + dp[nxt[i]][k - 1][0]
                ids = tuple(sorted((idx,) + dp[nxt[i]][k - 1][1]))

                if score > skip[0] or (score == skip[0] and ids < skip[1]):
                    dp[i][k] = (score, ids)
                else:
                    dp[i][k] = skip

        return list(dp[0][4][1])