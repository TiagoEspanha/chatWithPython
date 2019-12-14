import socket

host = '127.0.0.1'
porta = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((host, porta))
    
    while True:
        msg = input('Cliente:')
        cliente.sendall(msg.encode())

        msg_do_servidor = cliente.recv(1024)
        print(msg_do_servidor.decode())
    