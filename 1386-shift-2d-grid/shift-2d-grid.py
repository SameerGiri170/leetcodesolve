class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        arr = sum(grid, [])
        k %= len(arr)

        arr = arr[-k:] + arr[:-k]

        return [arr[i*n:(i+1)*n] for i in range(m)]