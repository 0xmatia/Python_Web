import socket


def main():
    IP = "127.0.0.1"
    PORT = 9011
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (IP, PORT)
    connection.connect(address)
    print(connection.recv(1024).decode())  # connection to server was successful


if __name__ == '__main__':
    main()