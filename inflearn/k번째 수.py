T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))
