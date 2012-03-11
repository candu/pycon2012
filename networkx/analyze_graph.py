import networkx
from graphapi import *
from likes import *
import time

init()
with open('friends_likes.graph') as f:
    G = load_edges(f)
for (d, a) in sorted([(d, a) for (a, d) in networkx.degree(G).iteritems()], reverse=True):
    if G.node[a]['type'] != 'page':
        continue
    if d < 10:
        break
    page = fetch('/{0}'.format(a))
    print d, page['name']
    time.sleep(0.1)
