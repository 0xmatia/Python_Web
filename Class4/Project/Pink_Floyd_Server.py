import socket


def main():
    PORT = 9011
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', PORT)
    listen_socket.bind(server_address)
    while True:
        listen_socket.listen(1)
        client_socket, client_address = listen_socket.accept()
        client_socket.sendall("Welcome to Pink Floyd database!".encode())


if __name__ == '__main__':
    main()

