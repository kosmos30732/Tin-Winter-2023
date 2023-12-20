# t = int(input())
# for _ in range(t):
#     n = int(input())
#     weights = list(map(int, input().split()))
#     if n==1 or n==2:
#         print("Yes")
#         continue
#     max_threshold=max(weights)
#     if max_threshold<n-1:
#         print("No")
#         continue
#     weights.sort(reverse=True)
#     total_edges = sum(weights)
#     max_possible_edges = (n - 1) * (weights[0])
#     if total_edges <= max_possible_edges:
#         print("Yes")
#     else:
#         print("No")

t = int(input())
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))

    weights.sort()
    max_edges = weights[-1]

    total_weight = sum(weights)
    if (total_weight % 2 == 0 and total_weight <= 2 * max_edges) or (total_weight <= (n-1)*max_edges):
        print("Yes")
    else:
        print("No")