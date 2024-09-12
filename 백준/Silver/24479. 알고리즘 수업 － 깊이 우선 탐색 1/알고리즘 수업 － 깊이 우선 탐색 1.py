import sys

sys.setrecursionlimit(10 ** 5)


def dfs(R):
    global cnt
    visited[R] = cnt
    path[R].sort()
    for i in path[R]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


N, M, R = map(int, input().split())
path = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 1
for _ in range(M):
    i, j = map(int, input().split())
    path[i].append(j)
    path[j].append(i)
dfs(R)
for i in range(1, N + 1):
    print(visited[i])
