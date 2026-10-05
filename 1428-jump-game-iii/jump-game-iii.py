class Solution:
    def canReach(self, arr, start):
        q = [start]
        seen = set()

        while q:
            i = q.pop()

            if i in seen:
                continue
            seen.add(i)

            if arr[i] == 0:
                return True

            if i + arr[i] < len(arr):
                q.append(i + arr[i])

            if i - arr[i] >= 0:
                q.append(i - arr[i])

        return False