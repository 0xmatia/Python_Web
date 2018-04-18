import socket


def main():
    SERVER_ADDRESS = "127.0.0.1"
    DEST_PORT = 8882
    MESSAGE = b"Elad Matia"
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create new socket

    address = (SERVER_ADDRESS, DEST_PORT)  # tuple with the connection information
    connection.connect(address)  # connect to server

    connection.sendall(MESSAGE)  # send a message
    server_response = connection.recv(1024)  # get server response
    server_response = server_response.decode()  # decode it
    print(server_response)  # print it


if __name__ == '__main__':
    main()
