k = int(input())
ml = []

for i in range(k):
    money = int(input())
    if money == 0:
        ml.pop()
    else:
        ml.append(money)
result = sum(ml)

print(result)