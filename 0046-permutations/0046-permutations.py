class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:

                if num not in curr:
                    curr.append(num)
                    print(f"before num is {num} and cur is {curr}")
                    backtrack(curr)
                    curr.pop()
                    print(f"after is num is {num} and cur is {curr}")
                else:
                    print(f"MATCH num is {num} and IT IS IN CUR which is cur is {curr}")


        ans = []
        backtrack([])
        return ans