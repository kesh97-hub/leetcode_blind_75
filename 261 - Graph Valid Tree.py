class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree Property:
        if len(edges) != n - 1:
            return False

        adjList = [[] for _ in range(n)]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = [False] * n

        queue = collections.deque()
        queue.append((0, -1))
        visited[0] = True

        while queue:
            curr, prev = queue.popleft()

            for neighbor in adjList[curr]:
                if neighbor == prev:
                    continue

                if visited[neighbor]:
                    return False
                
                queue.append((neighbor, curr))
                visited[neighbor] = True

        for i in range(n):
            if visited[i] == False:
                return False

        return True
