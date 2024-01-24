class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        count = len(arr1)
        sorted_arr2 = sorted(arr2)
        for num1 in arr1:
            for num2 in sorted_arr2:
                if abs(num1-num2) <=d:
                    count -= 1
                    break 
                else:
                    pass #can use continue here too
            
        return count