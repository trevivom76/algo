T = int(input())

for tc in range(1, T + 1):
    A, B, C = map(int, input().split()) # 굳이 리스트 필요 x

    if B < 2 or C < 3:       # A<B<C 구조를 만들 수 없는 케이스를 처리
        print(f'#{tc} -1')
        continue

    eat = 0 # 먹은 사탕 개수
    # 설계: B가 c 이상일 때, b = c - 1 이라면 최소 개수
    if B >= C:
        eat += B - (C - 1)      # 차이 만큼 먹는다.
        B = C - 1
    #       A 가 B 이상일 때, A = B - 1 이라면 최소 개수
    if A >= B:
        eat += A - (B - 1)
        A = B - 1

    print(f'#{tc} {eat}')
