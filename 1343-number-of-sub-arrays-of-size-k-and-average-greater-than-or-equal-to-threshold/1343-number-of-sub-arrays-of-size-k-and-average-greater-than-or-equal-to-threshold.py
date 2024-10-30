class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l = 0
        total = 0
        currentSum = 0
        
        for r in range(k):
            
            currentSum += arr[r]
        
        if (currentSum // k) >= threshold: 
            total += 1
        
        for r in range(k,len(arr)):
            
            currentSum += arr[r]
            currentSum -= arr[l]
     
            if (currentSum // k) >= threshold: 
                total += 1
            
            l += 1 
        
        return total

            
            
            
        