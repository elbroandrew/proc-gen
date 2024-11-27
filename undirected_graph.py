class UndirectedGraph:
    def __init__(self):
        self._adjacency_list = dict()

    @property
    def root(self):
        return next(iter(self._adjacency_list))  # returns only FIRST element

    def get_rooms(self):
        for room, values in self._adjacency_list.items():
            print(f"{room.id}:{[r.id for r in values]}")
        # return self._adjacency_list

    def add_vertex(self, vertex):
        if not vertex in self._adjacency_list.keys():
            self._adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self._adjacency_list.keys():
            if not v2 in self._adjacency_list[v1]:
                self._adjacency_list[v1].append(v2)
        else:
            self.add_vertex(v1)
            self._adjacency_list[v1].append(v2)

        if v2 in self._adjacency_list.keys():
            if not v1 in self._adjacency_list[v2]:
                self._adjacency_list[v2].append(v1)
        else:
            self.add_vertex(v2)
            self._adjacency_list[v2].append(v1)



    def dfs_recursive_traverse(self, start):
        result = []
        visited = {}

        def dfs(vertex):
            if not vertex:
                return None
            visited[vertex] = True
            result.append(vertex)
            for n in self._adjacency_list[vertex]:
                if not n in visited.keys():
                    dfs(n)
        dfs(start)
        return result

    def dfs_iterative_traverse(self, start):
        s = [start]  # we will use it like STACK, pop and append methods only
        visited = {}
        result = []
        visited[start] = True

        while s:
            vertex = s.pop()
            result.append(vertex)

            for n in self._adjacency_list[vertex]:
                if not n in visited.keys():
                    visited[n] = True
                    s.append(n)
        return result

    def bfs(self, start):
        # using list as queue
        q = list(start)
        visited = {start: True}
        result = []

        while q:
            v = q.pop(0)
            result.append(v)
            for n in self._adjacency_list[v]:
                if not n in visited.keys():
                    visited[n] = True
                    q.append(n)

        return result