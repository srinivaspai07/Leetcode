MOD = 10**9 + 7

def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        half_power = power(x, n // 2) % MOD
        return (half_power * half_power) % MOD
    else:
        half_power = power(x, (n - 1) // 2) % MOD
        return (half_power * half_power * x) % MOD

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_count = (n + 1) // 2  # Number of even positions
        odd_count = n // 2         # Number of odd positions
        
        even_power = power(5, even_count)
        odd_power = power(4, odd_count)
        
        return (even_power * odd_power) % MOD

