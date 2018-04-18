import socket
import time
import random


def main():
    SERVER_PORT = 1112
    SERVER_NAME = "Magshiserver"
    choices = ["TIME", "NAME", "RAND", "EXIT"]
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('', SERVER_PORT)
    main_socket.bind(server_address)  # create a server
    main_socket.listen(1)  # listen
    print("Now listening on port " + str(SERVER_PORT))

    client_socket, client_address = main_socket.accept()  # accepting a client connection
    while True:
        client_message = client_socket.recv(4096).decode()  # getting the client's message
        print(client_message)
        if client_message == choices[3]:
            break  # if the command is exit exit the loop amd close all sockets
        if client_message == choices[0]:
            current_time = time.strftime('%H:%M').encode()  # current time
            client_socket.sendall(current_time)
        elif client_message == choices[1]:  # server name
            server_message = SERVER_NAME.encode()
            client_socket.sendall(server_message)
        elif client_message == choices[2]:  # random number
            server_message = random.randint(1, 10)
            client_socket.sendall(str(server_message).encode())
    print("Loop terminated, shutting down sockets")
    client_socket.close()
    main_socket.close()


if __name__ == '__main__':
    main()
