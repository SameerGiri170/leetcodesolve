class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        dp = {0: 0}

        for i in range(m):
            valid = 0
            for j in range(n):
                if seats[i][j] == '.':
                    valid |= 1 << j

            ndp = {}

            for mask in range(1 << n):
                if mask & ~valid:
                    continue
                if mask & (mask << 1):
                    continue

                count = bin(mask).count('1')
                best = 0

                for prev, val in dp.items():
                    if mask & (prev << 1) or mask & (prev >> 1):
                        continue
                    best = max(best, val)

                ndp[mask] = best + count

            dp = ndp

        return max(dp.values())