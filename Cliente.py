import socket
import sys
#D@vidlanchero$
# Crear socket un TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al socket un puerto donde el Servidor Este en Modo Escucha
server_address = ('localhost', 5000)
print('Conectado con {} puerto {}'.format(*server_address))
sock.connect(server_address)

try:

    # Enviar el mensaje
    message = b'Prueba de conexion o chequeo de puerto. Este mensaje se repetira'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Observando la respuesta
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('Prueba de conexion o chequeo de puertos exitoso {!r}'.format(data))

finally:
    print('Fin de la prueba')
    sock.close()