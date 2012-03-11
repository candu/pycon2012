import networkx

def load_edges(f):
    G = networkx.Graph()
    for line in f:
        a, B = line.strip().split(' ', 1)
        a = int(a)
        B = map(int, eval(B))
        G.add_node(a, type='user')
        for b in B:
            G.add_node(b, type='page')
            G.add_edge(a, b)
    return G
