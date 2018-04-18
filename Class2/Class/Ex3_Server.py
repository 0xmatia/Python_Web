import socket
import time
import random


def main():
    SERVER_PORT = 8200
    SERVER_NAME = "Magshiserver"
    choices = ["TIME", "NAME", "RAND", "EXIT"]
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('', SERVER_PORT)
    main_socket.bind(server_address)  # create a server
    main_socket.listen(1)  # listen
    print("Now listening on port " + str(SERVER_PORT))

    client_socket, client_address = main_socket.accept()  # accepting a client connection
    client_message = client_socket.recv(4096).decode()  # getting the client's message
    while not client_message == choices[3]:
        if client_message == choices[0]:
            current_time = time.strftime('%H:%M').encode()  # current time
            client_socket.sendall(current_time)
        elif client_message == choices[1]:  # server name
            server_message = SERVER_NAME.encode()
            client_socket.sendall(server_message)
        elif client_message == choices[2]:  # random number
            server_message = random.randint(0, 10).encode()
            client_socket.sendall(server_message)
    client_socket.close() # close connection if user typed EXIT


if __name__ == '__main__':
    main()
