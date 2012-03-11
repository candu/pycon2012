import networkx
from graphapi import *

init(['friends_likes'])
uids = pull(fetch('/me/friends'), 'id')
for uid in uids:
    print uid, map(int, pull(fetch('/{0}/likes'.format(uid)), 'id'))
