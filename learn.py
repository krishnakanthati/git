from collections import deque

a = [[],[2,6],[1,3,4],[2],[2,5],[4,8],[1,7,9],[6,8],[5,7],[6]] # neighbors

n = 9 # starting node: 1
# 1 based indexing

q = deque()
q.append(1)

vis = [0] * (n+1)
vis[1] = 1

bfs = []

while q:
    node = q.pop()
    bfs.append(node)
    for i in a[node]:
        if not vis[i]:
            q.appendleft(i)
            vis[i] = 1
print(bfs)
