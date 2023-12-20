from collections import defaultdict

def count_marmots(n, m, edges, stickers, queries):
    adjacency_list = defaultdict(list)

    for v, u in edges:
        adjacency_list[v].append(u)
        adjacency_list[u].append(v)

    counts = [0] * (n + 1)
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            stack = [i]
            visited[i] = True

            while stack:
                node = stack.pop()
                counts[node] += stickers[node - 1]

                for neighbor in adjacency_list[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        visited[neighbor] = True

    result = []
    for query in queries:
        if query[0] == '?':
            result.append(counts[int(query[1])])
        else:
            v, x = int(query[1]), int(query[2])
            for neighbor in adjacency_list[v]:
                stickers[neighbor - 1] += x
                counts[neighbor] += x

    return result

n, m, q = map(int, input().split())
stickers = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]
queries = [input().split() for _ in range(q)]

results = count_marmots(n, m, edges, stickers, queries)
for res in results:
    print(res)
