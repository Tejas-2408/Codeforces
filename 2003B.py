def sol():
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    idx = int(n/2)
    print(l[idx])


t = int(input())
for _ in range(t):
    sol()