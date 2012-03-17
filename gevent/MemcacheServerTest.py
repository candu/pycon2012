from memcache import MemcacheService
from memcache.ttypes import *

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

import gevent
import random
import pprint
import optparse

def parse_args():
    parser = optparse.OptionParser()
    parser.add_option('--host', dest='host', default='localhost')
    parser.add_option('--port', type=int, dest='port', default=11111)
    parser.add_option('--iters', type=int, dest='iters', default=1000)
    parser.add_option('--clients', type=int, dest='clients', default=8)
    return parser.parse_args()

class MemcacheTestClient:
    def __init__(self, options):
        self._options = options
        self._socket = TSocket.TSocket(options.host, options.port)
        self._transport = TTransport.TFramedTransport(self._socket)
        self._protocol = TBinaryProtocol.TBinaryProtocol(self._transport)
        self._client = MemcacheService.Client(self._protocol)
        self._transport.open()

    def run(self):
        for i in range(self._options.iters):
            op = random.choice(['Set', 'Get'])
            if op == 'Set':
                key = ''.join(random.choice('abcdefghij') for i in range(4))
                value = str(random.randrange(0, 10))
                self._client.Set(key, value)
            elif op == 'Get':
                key = ''.join(random.choice('abcdefghij') for i in range(4))
                pprint.pprint(self._client.Get(key))
        self._transport.close()

def run_client(options):
    client = MemcacheTestClient(options)
    client.run()

def main():
    options, args = parse_args()
    gs = []
    for i in range(options.clients):
        g = gevent.spawn(run_client, options)
        gs.append(g)
    gevent.joinall(gs)

if __name__ == '__main__':
    main()
