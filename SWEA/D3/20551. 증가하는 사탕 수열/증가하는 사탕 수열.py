T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    a, b, c = map(int, input().split())

    if c <= b:
        # 조율 한다고 먹은거
        answer += b - c + 1
        # 사탕을 먹고 남은거
        b = b - (b - c + 1)

    if b <= a:
        answer += a - b + 1
        a = a - (a - b + 1)

    #가능한 방법이 아닐 경우
    if a <= 0 or b <= 0 or c <= 0:
        answer = -1

    print(f"#{test_case}", answer)