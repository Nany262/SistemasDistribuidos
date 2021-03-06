from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random

Tabla_uso = [0,0,0] #[c0,c1,c2]
Procesadores = ['1','1','1']

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
    def PedidoProcesador(self, cliente):
    	Tab_order = sorted(Tabla_uso)
        menor = Tab_order[0]
    	print menor, "menor"
    	if menor == Tabla_uso[cliente]:
    		if '1' in Procesadores:
    			pos = Procesadores.index('1')
    			Procesadores[pos] = 0
    			Tabla_uso[cliente] += 1
    			print Tabla_uso, "Si se asigno procesador"
    			print Procesadores, "Procesador"
    			return 1,pos
    	else:
    		Tabla_uso[cliente] -= 1
    		print Tabla_uso,"No se asigno procesador"
    		return 0,-1

    def DevolverProcesador(self, pos):
    	Procesadores[pos] = '1'
    	return 0

server.register_instance(MyFuncs())

server.serve_forever()
