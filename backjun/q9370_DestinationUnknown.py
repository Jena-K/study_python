import heapq
input=__import__('sys').stdin.readline
def dks(s):
    dist=[INF]*(n+1)
    dist[s]=0
    heap=[(0, s)]
    while heap :
        now=heapq.heappop(heap)[1]
        for new_dist, new_dest in data[now]:
            if (d := dist[now]+new_dist) < dist[new_dest]:
                dist[new_dest]=d
                heapq.heappush(heap, (d,new_dest))
    return dist

for _ in range(int(input())):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    data=[[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d=map(int, input().split())
        data[a].append((d, b))
        data[b].append((d, a))

    DU=sorted([int(input()) for _ in range(t)])
    INF=int(1e9)

    ds,dg,dh=dks(s),dks(g),dks(h)

    answer=[i for i in DU if ds[i]-dg[h] in [dg[s]+dh[i],dh[s]+dg[i]]]

    for i in answer:
        print(i, end=' ')
    print('')