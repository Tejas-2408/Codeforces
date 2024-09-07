def sol():
    n = int(input())
    s = input()
    if s[0] == s[-1]:
        print("No")
    else:
        print("Yes")


t = int(input())
for _ in range(t):
    sol()