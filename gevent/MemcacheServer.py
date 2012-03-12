from memcache import MemcacheService
from memcache.ttypes import *
from MemcacheHandler import MemcacheHandler

from TGEventServer import TGEventServer

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

import sys

PORT = 11111

def main():
    handler = MemcacheHandler()
    server = TGEventServer(
        MemcacheService.Processor(handler),
        TSocket.TServerSocket(port=PORT),
        TTransport.TFramedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory())
    print 'Starting server on port {0}...'.format(PORT)
    server.serve()
    print 'done.'

if __name__ == '__main__':
    main()
