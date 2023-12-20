n, q = map(int, input().split())
a = list(map(int, input().split()))

def apply_query(query):
    command = query[0]
    if command == '+':
        l, r, x = map(int, query[1:])
        for i in range(l - 1, r):
            a[i] += x
    elif command == '?':
        l, r, k, b = map(int, query[1:])
        result = float('-inf')
        for i in range(l - 1, r):
            result = max(result, min(a[i], k * (i + 1) + b))
        print(result)

for _ in range(q):
    query = input().split()
    apply_query(query)
