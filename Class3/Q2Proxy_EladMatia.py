import socket


def main():
    IP_ADDR = "54.71.128.194"
    PORT = 9090
    while True:  # loop forever (listen socket will wait until it receives a connection)
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('', PORT)
        listen_socket.bind(server_address)  # create a server
        listen_socket.listen(1)  # listen
        print("Now listening on port 9090")

        client_socket, client_address = listen_socket.accept()  # accepting a client connection
        client_message = client_socket.recv(1024).decode()  # getting the client's message
        print("Film4me message: " + client_message)
        # do nothing go on!
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (IP_ADDR, 92)
        send_socket.connect(address)
        send_socket.sendall(client_message.encode())

        # modify the server response - fix the picture and add proxy to movie name
        server_response = send_socket.recv(1024).decode()
        if not server_response[:5] == "ERROR":
            server_response = server_response[:len(server_response)-11]+"."+server_response[len(server_response)-11:]  # assemble the new request
            server_response = server_response[:16] + "Proxy" + server_response[16:]
        # modify servererror to error
        if server_response[:6] == "SERVER":
            server_response = server_response[6:]
        print(server_response)  # new client request
        client_socket.sendall(server_response.encode())
        send_socket.close()
        client_socket.close()
        listen_socket.close()


if __name__ == '__main__':
    main()