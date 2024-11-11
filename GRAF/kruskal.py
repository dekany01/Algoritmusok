import sys

def kruskals(g_nodes, g_from, g_to, g_weight):

    edges = []

    for i in range(len(g_from)):
        edges.append([g_from[i],g_to[i],g_weight[i]])

    edges = sorted (edges, key=lambda list : (list[0]+list[1]))
    edges = sorted (edges, key=lambda list : list[2] )
    print(edges)

    setID = {}
    for j in range(g_nodes):
        setID[j+1] = j+1

    print(setID)
    def findSet(node):
        return setID[node]

    def settingID(maximum,minimum):
        old_value = findSet(maximum)
        new_value = findSet(minimum)

        for id in setID:
            if  setID[id] == old_value :
                setID[id] = new_value

    totalWeight = 0

    for edge in edges:
        if findSet(edge[0]) != findSet(edge[1]):
            totalWeight += edge[2]
            settingID(max(edge[0],edge[1]),min(edge[0],edge[1]))
        print(setID)
        print(totalWeight)

    return totalWeight

def main():
    input = sys.stdin.readlines()
    firstLine = input[0].split()
    g_nodes = int(firstLine[0])
    m = int(firstLine[1])

    g_from = []
    g_to = []
    g_weight = []


    for i in range (1,m+1):
        line = input[i].split()

        g_from.append(int(line[0]))
        g_to.append(int(line[1]))
        g_weight.append(int(line[2]))
    #print(g_nodes)
    #print(g_from)
    #print(g_to)
    #print(g_weight)
    kruskals(g_nodes,g_from,g_to,g_weight)

if __name__ == "__main__":
    main()
