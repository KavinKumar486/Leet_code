from collections import defaultdict
class Solution:
    
    def topoSort(self, V, edges):
        visited = [0]*len(edges)
        res=[]
        adj=defaultdict(list)
        def dfs(node):
            if not visited[node]:
                visited[node] = 1
            else:
                return
            for i in adj[node]:
                dfs(i)
                res.append(node)
        for i,j in edges:
            adj[i].append(j)
        for i in adj:
            dfs(i)
        return res
