import heapq
from collections import defaultdict


def solve():
    N, M = map(int, input().split())
    adj = defaultdict(list)

    # create adjecency list
    for _ in range(M):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    # created needed datastrucutres to run prims algorithm
    # visited set to not create cycles
    visited = set()
    # random start node
    start_node = next(iter(adj))
    # min heap with value 0
    min_heap = [(0, start_node)]
    mst_cost = 0

    # prims algorithm
    while min_heap and len(visited) < N:
        # pop the weight and node
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        # add to visited and add cost to mst_cost
        visited.add(node)
        mst_cost += weight

        # push new neighbours to heap from the recently popped node
        for neighbor, edge_weight in adj[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))

    print(mst_cost)


if __name__ == "__main__":
    solve()
