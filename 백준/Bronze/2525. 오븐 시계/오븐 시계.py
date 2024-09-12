A, B = map(int, input().split())
C = int(input())
A1 = A + ((B + C) // 60)
B1 = B + C

if B1 >= 60:
    A = A1
    B = B1 - 60 * ((B + C) // 60)
    if A >= 24:
        A = A - 24

elif B1 < 60:
    B = B1

print(A, B)
