class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        results = []
    
        def backtrack(index,cur,k):
        
        
            if len(cur) == k:
                results.append(cur.copy())
            
            for i in range(index,n+1):
            
                cur.append(i)
                backtrack(i+1,cur,k)
                cur.pop()
    
        backtrack(1,[],k)
        return results
        