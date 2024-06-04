class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):

            print(f"open is {openN} and close is {closedN}")
            print(stack)

            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                print(f"initial checking {openN} and {closedN}")
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                print(f"inside checking {openN} and {closedN}")
                stack.pop()

        backtrack(0, 0)
        return res