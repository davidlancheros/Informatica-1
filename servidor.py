import socket
import sys
#D@vidlanchero$
# Crear un TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket con el pueto
server_address = ('localhost', 5000)
print('Inicializando conexion con {} port {}'.format(*server_address))
sock.bind(server_address)

# Modo escucha
sock.listen(1)

while True:
    # Esperando  conexion
    print('Esperando  conexion')
    connection, client_address = sock.accept()
    try:
        print('Conectado desde', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('Recibido {!r}'.format(data))
            if data:
                print('Enviado prueba de vuelta')
                connection.sendall(data)
            else:
                print('Data no recibida', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()