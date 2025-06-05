class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i > j:
            self.id[i] = j
        else:
            self.id[j] = i

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        for a, b in zip(s1, s2):
            uf.union(ord(a) - ord('a'), ord(b) - ord('a'))
        
        return ''.join(chr(uf.find(ord(c) - ord('a')) + ord('a')) for c in baseStr)
