a, b, c = map(int, input().split())

d = 0
if a == b and b == c and c == a:
    d = 10000 + a * 1000
elif (a == b and b != c) or (a != b and b == c):
    d = 1000 + b * 100
elif (a == c and a != b):
    d = 1000 + a * 100

else:
    d = max(a, b, c) * 100

print(d)