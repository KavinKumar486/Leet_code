from collections import defaultdict
class Solution:    

    def topoSort(self, V, edges):
        visited = [0]*V
        adj=defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        res=[]
       
        def dfs(node):
            visited[node]= 1
            for i in adj[node]:
                if not visited[i]:
                    dfs(i)
            res.append(node)
        for node in range(V):
            if not visited[node]:
                dfs(node)
        return res[::-1]
s= Solution()
V=4
edges =[[3, 0], [1, 0], [2, 0]]
print(s.topoSort(V,edges))