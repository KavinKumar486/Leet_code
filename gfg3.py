from collections import defaultdict
class Solution:
    def isCycle(self, V, edges):
        #Code here
        seen=set()
        cur_stack=set()
        def dfs(node,cur_stack):
            seen.add(node)
            cur_stack.add(node)
            for i in adj[node]:
                if i not in seen:
                    dfs(i,cur_stack)
                elif i in cur_stack:
                    return True
            cur_stack.remove(node)
            return False
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(V+1):
            if i not in seen:
                if dfs(i,cur_stack):
                    return True
        return False
