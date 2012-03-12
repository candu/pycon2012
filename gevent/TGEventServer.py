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
            while True:
                self.processor.process(iprot, oprot)
        except TTransport.TTransportException, e:
            pass
        itrans.close()
        otrans.close()

    def serve(self):
        self.serverTransport.listen()
        while True:
            try:
                client = self.serverTransport.accept()
                gevent.spawn(self.handle, client)
            except KeyboardInterrupt:
                raise
            except Exception, e:
                logging.exception(e)
