T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N x N 행렬
    arr = [input() for _ in range(N)]

    # is_square 함수의 로직을 직접 구현
    n = len(arr)
    # top, bottom, left, right 초기화
    top = left = n  # 가장 큰 값으로 초기화
    bottom = right = -1  # 가장 작은 값으로 초기화

    # 2차원 배열 순회하며 정사각형의 가장자리 계산
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':  # '#'을 발견하면
                top = min(top, i)  # 가장 위쪽 갱신
                left = min(left, j)  # 가장 왼쪽 갱신
                bottom = max(bottom, i)  # 가장 아래쪽 갱신
                right = max(right, j)  # 가장 오른쪽 갱신

    # 높이와 너비가 같지 않으면 정사각형이 아님
    if bottom - top != right - left:
        result = 'no'
    else:
        # 정사각형 내부의 모든 칸이 '#'으로 채워져 있는지 확인
        square_valid = True
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                if arr[i][j] != '#':  # '#'이 아닌 칸이 있으면 정사각형이 아님
                    square_valid = False
                    break
            if not square_valid:
                break

        result = 'yes' if square_valid else 'no'

    print(f'#{tc} {result}')
