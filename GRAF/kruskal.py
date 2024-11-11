import sys

def kruskals(g_nodes, g_from, g_to, g_weight):

    # Kruskal algoritmus segítségével oldható meg a feladat.
    
    edges = []  # Az éleket tartalmazó lista

    for i in range(len(g_from)):    
        edges.append([g_from[i],g_to[i],g_weight[i]])   # Bele tesszük a paraméterben kapott tömbök i. értékeit egy listába
                                                        # A lista az adott élt reprezentálja, melyet eltárolunk az 'edges' listában.

    edges = sorted (edges, key=lambda list : (list[0]+list[1])) # Rendezzük az éleket először az első két szám (a csúcsok) összege alapján.
    edges = sorted (edges, key=lambda list : list[2] )           # Majd rendezzük a súlyuk alapján is.
    

    setID = {}        # Létrehozunk egy dictionary-t, ami tárolja, hogy az adott csúcs, melyik részgráfhoz tartozik. (kulcs = adott csúcs, érték = részgráf azonosítószáma)
    for j in range(g_nodes):
        setID[j+1] = j+1    # Mivel kezdetben minden csúcs önmagában részgráf, ezért létrehozunk annyi elemet, amennyi db csúcs van.

   
    def findSet(node):
        return setID[node]   # a részfüggvény egyszerűen visszaadja, hogy az adott csúcs melyik részgráfban található.

    def settingID(maximum,minimum):    # ez a részfüggvény egyesíti a két részgráfot gyakorlatilag (ugyanaz lesz innentől az azonosítójuk)
        # a függvény a kapott maximum és minimum érték alapján először megnézi:
    
        old_value = findSet(maximum)    # megkeresi, hogy a vizsgált két csúcs közül a nagyobb számúnak jelenleg mi az értéke (melyik részgráfhoz tartozik)
        new_value = findSet(minimum)    # megkeresi, hogy a vizsgált két csúcs közül a kisebbik számúnak jelenleg mi az értéke (melyik részgráfhoz tartozik)

        for id in setID:                    
            if  setID[id] == old_value :      # a részfüggvény ezután megkeresi az összes olyan csúcsot, melyek értéke a nagyobb számú csúcséval egyenlő (tehát egyazon részgráfhoz tartoznak)  
                setID[id] = new_value        # majd beállítja mindegyik ilyen kulcsnak az értékét az új értékre (a kisebb számú csúcs részgráfjának azonosítójára)

    totalWeight = 0  # ebben a változóban tároljuk az összes él súlyát

    for edge in edges:                            # a fentebb kapott rendezett lista elemein sorban végig megyünk
        if findSet(edge[0]) != findSet(edge[1]):        # ha a vizsgált él két pontja (vagy csúcsa) különböző részgráfokban találhatóak
            totalWeight += edge[2]                        # az adott él súlyával növeljük az összes él súlyát
            settingID(max(edge[0],edge[1]),min(edge[0],edge[1]))  # majd egyesítjük a két részgráfot
    

    return totalWeight  # végül visszaadja a teljes súlyt

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
    print(kruskals(g_nodes,g_from,g_to,g_weight))

if __name__ == "__main__":
    main()
