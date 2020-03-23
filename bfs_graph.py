from queue import Queue


def bfs_check(start=0):
    global visited
    q = Queue(len(gr))
    visited[start] = 1
    q.put(start)
    while not q.empty():
        node = q.get()
        for vertex in gr[node]:
            if visited[vertex] == 0:
                visited[vertex] = -1*visited[node]
                q.put(vertex)
            elif visited[vertex] == visited[node]:
                print("Graph is not bipartite")
                return "Graph is not bipartite"
        while True:
            for ind, i in enumerate(visited):
                if i == 0:
                    start = ind
                    bfs_check(start)
                    break
            break
    return "Graph is bipartite"


if __name__ == "__main__":
    #gr = [[1, 2], [2, 3, 4], [], [], []]
    gr = [[1, 2], [3, 4], [], [], [], [6], [7], [5]]
    #gr = [[1, 2], [3, 4], [], [], [], [6], [], []]
    visited = [0] * len(gr)
    print(bfs_check(0))

