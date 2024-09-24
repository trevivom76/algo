nm = []

for i in range(9):
    n = int(input())
    nm.append(n)

print(max(nm))
print(nm.index(max(nm))+1)