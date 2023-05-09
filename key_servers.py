from collections import defaultdict

num_vertices = 0
num_servers = 0
servers_list = []
tot_sum = 0
new_servers_list = []

class Stack:
  def __init__(self):
    self.storage = []
  def isEmpty(self):
    return len(self.storage) == 0
  def push(self, node):
    self.storage.append(node)
  def pop(self):
    return self.storage.pop()


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, time):
        self.graph[u].append([v, time])

    # depth first search traversal
    def DFS(self):

        # Mark the current node as visited and print it
        visited = [False] * g.V
        stack = Stack()
        stack.push(servers_list[0])
        visited[servers_list[0]] = True

        while (not stack.isEmpty()):
            node = stack.pop()
            nbrs = g.graph[node]
            # print("CURRENT NODE")
            # print("The node", node, "The neighbours", nbrs)

            # The function will check if the vertex is a leaf or not recursively
            reduce_graph(node, nbrs)

            for n in nbrs:
                if not visited[n[0]]:
                    stack.push(n[0])
                    visited[n[0]] = True


# Recursive function which deletes all leaves from the tree so that we have only the shortest path nodes left in graph
def reduce_graph(k,v):
    global servers_list

    # if k not in servers_list:
    if not search_for_k(sorted_servers, k):
        if len(v) == 1:
            for i in g.graph[(v[0][0])]:
                if i == [k, v[0][1]]:
                    # print("Deleting", i, "from", g.graph[v[0][0]])
                    g.graph[v[0][0]].remove(i)
                    # print("After removing values", v[0][0], g.graph[v[0][0]])
                    # print(v[0][0]) # 11
                    # print(g.graph[v[0][0]])

                    n = v[0][0]
                    m = g.graph[v[0][0]]
                    # g.graph.pop(v[0][0])
                    reduce_graph(n, m)
                    # if v[0][0] not in servers_list and len(g.graph[v[0][0]]) == 1:
                    #     # print(g.graph[v[0][0]])
                    #     for i in g.graph[v[0][0]]:
                    #         # print(i[0]) # 12
                    #         for n in g.graph[i[0]]:
                    #             if n == [v[0][0], i[1]]:
                    #                 g.graph[i[0]].remove(n)



            # print("Deleting", k, "from dictionary")
            g.graph.pop(k)

#The function will check if k is in the servers list
def search_for_k(sorted_servers,k,low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = num_servers-1

    if high < low:
        return False

    midpoint = (low+high) // 2

    if sorted_servers[midpoint] == k:
        return True
    elif k < sorted_servers[midpoint]:
        return search_for_k(sorted_servers,k, low, midpoint-1)
    else:
        return search_for_k(sorted_servers,k, midpoint+1, high)


def create_graph(dir):
    global num_vertices
    global num_servers
    global servers_list

    line_number = 0

    file = open(dir, 'r')
    for line in file:
        if line_number == 0:
            num_vertices, num_servers = line.split(" ")
            num_vertices = int(num_vertices)
            num_servers = int(num_servers)
            # print(num_vertices, num_servers)
            g.V = num_vertices

        elif line_number == 1:
            templine = line.strip()
            servers_list = templine.split(" ")
            servers_list = [int(i) for i in servers_list]

        else:
            templine = line.strip("\n")
            v1, v2, time = templine.split(" ")
            v1 = int(v1)
            v2 = int(v2)
            time = int(time)
            # print(v1,v2,time)
            g.addEdge(v1,v2,time)
            g.addEdge(v2, v1, time)


        line_number += 1
    file.close()


def calculate_path_sum(g):

    sum = 0
    for k,v in list(g.graph.items()):
        # print(k,v)
        for i in g.graph[k]:
            # print(i)
            # print(i[1])
            sum += i[1]
    print(sum)


g = Graph(num_vertices)
create_graph('./pubdata_key_servers/pub10.in')
sorted_servers = sorted(servers_list)
# print(search_for_k(sorted_servers, 0))

# print(servers_list.sorted())
# servers_list = servers_list.sort()
# search_for_k(servers_list,2)
# print(g.graph)
g.DFS()
# print(g.graph)
calculate_path_sum(g)
# print(g.graph)