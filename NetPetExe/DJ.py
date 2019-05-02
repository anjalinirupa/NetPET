def main():
    x=input("Enter Number of nodes: ")
    y = input("distance from a to b: ")
    z = input("distance from a to c: ")
    v = input("distance from a to d: ")
    w = input("distance from b to c: ")
    u = input("distance from b to d: ")
    t = input("distance from c to d: ")
    graph = {'a':{'b':int(y),'c':int(z),'d':int(v)},'b':{'c':int(w),'a':int(y),'d':int(u)},'c':{'a':int(z),'b':int(w),'d':int(t)},'d':{'a':int(v),'b':int(u),'c':int(t)}}
    p=input("enter start node: ")
    q = input("enter destination node: ")

    dijkstra(graph, p, q)
 
def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
 
 
if __name__ == '__main__':
    main()
