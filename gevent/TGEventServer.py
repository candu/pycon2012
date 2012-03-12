import gevent
from thrift.server.TServer import TServer
from thrift.transport import TSocket, TTransport

import gevent.socket
TSocket.socket = gevent.socket

class TGEventServer(TServer):
    def __init__(self, *args, **kwargs):
        TServer.__init__(self, *args)

    def handle(self, client):
        itrans = self.inputTransportFactory.getTransport(client)
        otrans = self.outputTransportFactory.getTransport(client)
        iprot = self.inputProtocolFactory.getProtocol(itrans)
        oprot = self.outputProtocolFactory.getProtocol(otrans)
        try:
            print 'processing...'
            i = 0
            while True:
                self.processor.process(iprot, oprot)
                print 'received block {0}'.format(i)
                i += 1
        except TTransport.TTransportException, e:
            pass
        print 'done processing.'
        itrans.close()
        otrans.close()

    def serve(self):
        self.serverTransport.listen()
        while True:
            try:
                print 'accepting...'
                client = self.serverTransport.accept()
                print 'accepted client.'
                gevent.spawn(self.handle, client)
            except KeyboardInterrupt:
                raise
            except Exception, e:
                logging.exception(e)
