class Solution:
    def reverseParentheses(self, s):
        stack = []

        for ch in s:
            if ch == ')':
                temp = ""
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                stack += temp
            else:
                stack.append(ch)

        return ''.join(stack)