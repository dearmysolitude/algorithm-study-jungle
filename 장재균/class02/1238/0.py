import sys
import heapq
input = sys.stdin.readline
INF = int(1e9) #무한의 값

n,m,x = map(int,input().split())
graph = [[] for i in range(n+1)]

distance = [INF] *(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
value=[0]*(1+n)

for i in range(1,n+1):
    if i == x:
        continue
    distance = [INF] * (n + 1)
    dijkstra(i)
    value[i] = distance[x]
    distance = [INF] * (n + 1)
    dijkstra(x)
    value[i] += distance[i]

print(max(value))