class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r, c, size):
            val = grid[r][c]

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        half = size // 2
                        return Node(
                            True, False,
                            build(r, c, half),
                            build(r, c + half, half),
                            build(r + half, c, half),
                            build(r + half, c + half, half)
                        )

            return Node(bool(val), True, None, None, None, None)

        return build(0, 0, len(grid))
        