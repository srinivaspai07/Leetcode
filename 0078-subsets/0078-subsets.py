class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        cur = []
        def backtrack(i):

            if i >=len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            print(f"first backtrack is {i} and cur is {cur}")

            backtrack(i+1)

            cur.pop()
            print(f"just before second backtrack is {i} and cur is {cur}")      
            backtrack(i+1)
            print(f"after backtrack is {i} and cur is {cur}")

        backtrack(0)
        return res


        
        