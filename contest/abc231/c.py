import bisect
n,q = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
for _ in range(q):
    x = int(input())
    idx = bisect.bisect_left(a,x)
    print(n-idx)
