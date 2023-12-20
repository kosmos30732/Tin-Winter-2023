check_tin={"T":1, "I":1, "N":1, "K":1, "O":1, "F":2}
num=int(input())
f=True
for _ in range(num):
    f=True
    in_str=input()
    tmp=check_tin.copy()
    len_in_str=len(in_str)
    if len_in_str>7 or len_in_str<7:
        print("No")
        continue
    for j in range(len_in_str):
        if tmp.get(in_str[j])==None:
            f=False
            break
        else:
            tmp[in_str[j]]-=1
    if f:
         for j in tmp.values():
            if j !=0:
                f=False
                break
    if f:
        print("Yes")
    else:
        print("No")