T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = []

    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                lst.append(cnt)
            elif arr[i][j] == 0:
                cnt = 0

    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                lst.append(cnt)
            elif arr[i][j] == 0:
                cnt = 0
    lst = max(lst)

    print(f'#{tc} {lst}')