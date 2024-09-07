def sol():
    n = int(input())
    l = list(map(int,input().split()))
    e_s = sum(l[::2])
    o_s = sum(l[1::2])
    print(e_s-o_s)


t = int(input())

for _ in range(t):
    sol()