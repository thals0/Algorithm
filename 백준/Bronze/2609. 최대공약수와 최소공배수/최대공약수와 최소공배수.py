from math import gcd

a,b = map(int, input().split())

gcd = gcd(a, b)
lcm = a*b/gcd

print(gcd)
print(int(lcm))