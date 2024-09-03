# 입력
n, m = map(int, input().split())
# 리스트 초기화
arr = []
# 중심 노드 0으로 설정
node = 0

# 리프 노드를 중심 노드에 연결
for i in range(1, m + 1):
    arr.append((node, i))

# 나머지 노드들을 트리의 다른 노드에 연결
for i in range(m + 1, n):
    arr.append((i - 1, i))

# 출력
for line in arr:
    print(line[0], line[1])
