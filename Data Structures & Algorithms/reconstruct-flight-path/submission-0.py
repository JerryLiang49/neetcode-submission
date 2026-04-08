class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)

        result = ["JFK"]
        def dfs(source):
            if len(result) == len(tickets) + 1:
                return True
            if source not in graph:
                return False

            temp = list(graph[source])
            for i, nei in enumerate(temp):
                graph[source].pop(i)
                result.append(nei)
                if dfs(nei):
                    return True
                graph[source].insert(i, nei)
                result.pop()
            return False

        dfs("JFK")
        return result