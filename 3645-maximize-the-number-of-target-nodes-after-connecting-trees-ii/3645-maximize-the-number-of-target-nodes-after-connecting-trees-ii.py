from collections import deque
from typing import List, Optional

class Solution:
    # A single BFS that:
    # 1) returns the number of nodes on even-numbered levels, and
    # 2) if `included` is non-null, marks exactly those nodes at even levels
    def bfs(self, start: int, adj: List[List[int]], included: Optional[List[bool]] = None) -> int:
        q = deque()
        q.append((start, -1))
        count = 0
        level = 0

        while q:
            size = len(q)
            # on even levels we both add to count and (optionally) record the nodes
            if level % 2 == 0:
                count += size

            for _ in range(size):
                curr, parent = q.popleft()
                if included is not None and level % 2 == 0:
                    # mark this node as "included"
                    included[curr] = True
                for v in adj[curr]:
                    if v == parent:
                        continue
                    q.append((v, curr))
            level += 1
        return count

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # build adjacency lists
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        adj1 = [[] for _ in range(n1 + 1)]
        adj2 = [[] for _ in range(n2 + 1)]

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # Step-1: Find the best you can do by adding the extra edge in tree-2
        even_count2 = self.bfs(0, adj2)            # count of even-level nodes
        odd_count2 = n2 - even_count2               # the rest are odd-level
        best2 = max(even_count2, odd_count2)

        # Step-2: Run BFS on tree-1, and record nodes on even levels
        included = [False] * n1
        even_count1 = self.bfs(0, adj1, included)

        # Step-3: For each i, if i was even-level in tree-1 we connect it to tree-2's best even-level
        ans = [0] * n1
        for i in range(n1):
            if included[i]:
                # it contributes even_count1 from tree-1 plus best2 from tree-2
                ans[i] = even_count1 + best2
            else:
                # it would be odd in tree-1, so you get (n1-even_count1) + best2
                ans[i] = (n1 - even_count1) + best2
        return ans