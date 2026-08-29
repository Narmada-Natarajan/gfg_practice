class Solution:
    def prime_Sum(self, n):

        total = 0

        for x in range(2,n+1):

            is_prime = True

            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    is_prime = False
                    break

            if is_prime:
                total += x

        return total