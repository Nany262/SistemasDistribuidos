import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 9003
BUFFER_SIZE = 1024

print "Digite la operacion a realizar(Solo 2 numeros):"
Numero1=raw_input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(Numero1)
data = s.recv(BUFFER_SIZE)
s.close()

port,ip=data.split("?")
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((ip,int(port)))
s1.send(Numero1)
resultado = s1.recv(BUFFER_SIZE)
s1.close()

if data!="3":
	print "El resultado de la operacion es:", resultado
	print "La direccion IP es: ", ip
	print "El puero usado es: ", port

