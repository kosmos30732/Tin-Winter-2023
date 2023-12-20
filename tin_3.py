n, m = map(int, input().split())
prices = list(map(int, input().split()))

max_bur=0

for i in range(1,m+1):
    tmp=i
    for j in prices:
        if j<=tmp:
            tmp-=j
            if tmp==0:
                break
    max_bur=max(tmp,max_bur)
print(max_bur)