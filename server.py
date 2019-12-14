import socket

host = '127.0.0.1'
porta = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
	servidor.bind((host, porta))
	servidor.listen()
	conexao, addr = servidor.accept()
	print('Alguem conectou')

	with conexao:
		while True:
			msg_cliente = conexao.recv(1024)
			print(msg_cliente.decode())

			msg_servidor = input("SERVIDOR: ")
			conexao.sendall(msg_servidor.encode())
    

