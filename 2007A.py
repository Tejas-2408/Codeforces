def sol():
    l,r = map(int,input().split())
    cnt = 0
    for i in range(l,r+1):
        if i%2!=0:
            cnt+=1
    
    print(int(cnt/2))


t=int(input())

for _ in range(t):
    sol()