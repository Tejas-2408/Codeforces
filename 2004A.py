def sol():
    n = int(input())
    l = list(map(int,input().split()))
    if n>2:
        print("No")
    else:
        if l[1]-l[0]!=1:
            print("Yes")
        else:
            print("No")



t = int(input())
for _ in range(t):
    sol()