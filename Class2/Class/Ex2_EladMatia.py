import socket


def main():
    LISTENING_PORT = 8882
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
    server_address = ('', LISTENING_PORT)
    connection.bind(server_address)  # bind the socket to a port

    connection.listen(1)  # connect to a socket
    print("Listening now...")
    client_socket, client_address = connection.accept()  # accepting a client connection
    client_message = client_socket.recv(1024)  # getting the clients message
    client_message = client_message.decode()
    print("Message received, sending response")
    server_message = "You are " + client_message
    client_socket.sendall(server_message.encode())  # send the decoded message

    # close all sockets
    connection.close()
    client_socket.close()


if __name__ == '__main__':
    main()
