from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for num in candidates:
                if num >= start:
                    # add the number into the combination
                    comb.append(num)
                    # give the current number another chance, rather than moving on
                    backtrack(remain - num, comb, num)
                    # backtrack, remove the number from the combination
                    comb.pop()

        backtrack(target, [], 0)

        return results
