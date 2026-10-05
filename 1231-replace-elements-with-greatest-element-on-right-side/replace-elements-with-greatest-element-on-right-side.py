class Solution:
    def replaceElements(self, arr):
        mx = -1

        for i in range(len(arr)-1, -1, -1):
            x = arr[i]
            arr[i] = mx
            mx = max(mx, x)

        return arr