from collections import defaultdict

def dfs(node, companies, costs, graph, visited):
    visited[node] = True
    companies.add(costs[node])
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, companies, costs, graph, visited)

def find_min_cost(node, graph, costs, target_companies):
    min_cost = float('inf')
    visited = [False] * (len(graph) + 1)
    for company in target_companies:
        visited = [False] * (len(graph) + 1)  
        companies = set()
        dfs(node, companies, costs, graph, visited)
        if len(companies) == len(target_companies):
            total_cost = sum(costs[vertex] for vertex in companies)
            min_cost = min(min_cost, total_cost)
    return min_cost if min_cost != float('inf') else -1

def main():
    n, k = map(int, input().split())
    company_names = [input() for _ in range(k)]
    company_indices = {company_names[i]: i + 1 for i in range(k)}
    graph = defaultdict(list)
    costs = {}
    for i in range(1, n + 1):
        p, cost, company = input().split()
        p = int(p)
        cost = int(cost)
        if p == 0:
            root = i
        graph[p].append(i)
        graph[i]  
        costs[i] = company_indices[company]
    result = find_min_cost(root, graph, costs, set(company_indices.values()))
    print(result+1)

if __name__ == "__main__":
    main()
