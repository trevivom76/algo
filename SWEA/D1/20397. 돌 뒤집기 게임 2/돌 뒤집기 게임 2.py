T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1 # 인덱스를 0부터 시작

        left = i - 1
        right = i + 1

        for _ in range(j):
            if 0 <= left and right < N and stones[left] == stones[right]:
                stones[left] = 1 - stones[left] # 돌 뒤집기
                stones[right] = 1 - stones[right] # 돌 뒤집기
            left -= 1
            right += 1
    print(f'#{tc}', *stones)