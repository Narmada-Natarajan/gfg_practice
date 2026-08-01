class Solution:
    def gcd(self, a, b):
        
        while b!=0:
            a,b=b,a%b #a=3,b=6 -> a=6,b=3%6=0 ->as b=0 print a
        return a
        