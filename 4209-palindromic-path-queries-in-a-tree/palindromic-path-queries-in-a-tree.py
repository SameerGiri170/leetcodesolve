from typing import List
from collections import defaultdict

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length()
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        up = [[0] * LOG for _ in range(n)]
        pref = [0] * n
        timer = 0

        stack = [(0, -1, 0)]

        while stack:
            v, p, state = stack.pop()

            if state == 0:
                tin[v] = timer
                timer += 1

                if p != -1:
                    depth[v] = depth[p]
                    depth[v] += 1
                    pref[v] = pref[p] ^ (1 << (ord(s[v]) - 97))

                else:
                    pref[v] = 1 << (ord(s[v]) - 97)

                up[v][0] = v if p == -1 else p

                for j in range(1, LOG):
                    up[v][j] = up[up[v][j - 1]][j - 1]

                stack.append((v, p, 1))

                for w in reversed(g[v]):
                    if w != p:
                        stack.append((w, v, 0))

            else:
                tout[v] = timer

        bit = [0] * (n + 1)

        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def get(i):
            i += 1
            val = 0
            while i > 0:
                val ^= bit[i]
                i -= i & -i
            return val

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            d = depth[u] - depth[v]

            for j in range(LOG):
                if d & (1 << j):
                    u = up[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        s = list(s)
        ans = []

        for q in queries:
            a = q.split()

            if a[0] == "update":
                v = int(a[1])
                new = a[2]
                oldmask = 1 << (ord(s[v]) - 97)
                newmask = 1 << (ord(new) - 97)
                change = oldmask ^ newmask

                add(tin[v], change)
                add(tout[v], change)
                s[v] = new

            else:
                u, v = int(a[1]), int(a[2])
                w = lca(u, v)

                mask = (pref[u] ^ get(tin[u])) ^ (pref[v] ^ get(tin[v]))
                mask ^= 1 << (ord(s[w]) - 97)

                ans.append(mask == 0 or (mask & (mask - 1)) == 0)

        return ans