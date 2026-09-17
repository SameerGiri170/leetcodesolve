class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = {}

        for x in arr1:
            count[x] = count.get(x, 0) + 1

        ans = []

        for x in arr2:
            ans += [x] * count[x]
            del count[x]

        for x in sorted(count):
            ans += [x] * count[x]

        return ans