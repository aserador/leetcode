class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parentheses if number of open < n
        #only add closing if closed < open
        #stop when open == closed == n

        stack = []
        ans = []

        def backtrack(open, closed):
            if open == closed == n:
                ans.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()
        
        backtrack(0,0)
        return ans