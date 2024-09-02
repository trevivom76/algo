def calculate_change(N):
    coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = []

    for coin in coins:
        cnt = N // coin
        N %= coin
        change.append(cnt)

    return change

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = calculate_change(N)
    print(f'#{tc}')
    print(*result)