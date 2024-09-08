
def min_changes(arr):
    N = len(arr)
    M = len(arr[0])

    counts = [[row.count('W'), row.count('B'), row.count('R')] for row in arr]
    min_change = float('inf')

    # 중첩 for문 순회할때 경계를 잘 확인 i, j를 이용해서 색깔 영역을 잘 나눈다
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            change = 0
            # 흰색 영역
            change += sum(M - count[0] for count in counts[:i])
            # 파란색 영역
            change += sum(M - count[1] for count in counts[i:j])
            # 빨간색 영역
            change += sum(M - count[2] for count in counts[j:])

            min_change = min(min_change, change)

    return min_change

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N x M 행렬
    arr = [input() for _ in range(N)]
    result = min_changes(arr)
    print(f'#{tc} {result}')

