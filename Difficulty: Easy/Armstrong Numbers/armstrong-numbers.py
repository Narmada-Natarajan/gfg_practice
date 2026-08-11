class Solution:
    def armstrongNumber(self, n):
        temp = n
        digits = 0

        # Count digits
        while temp > 0:
            digits += 1
            temp //= 10
            
        temp=n
        total = 0

        # Calculate Armstrong sum
        while temp > 0:
            digit = temp % 10
            total += digit ** digits
            temp //= 10

        return total == n