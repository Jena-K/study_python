input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    [map(int, input().split()) for _ in range(m)]
    print(n-1)
        
