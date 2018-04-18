import socket


def main():
    SERVER_ADDRESS = "127.0.0.1"
    DEST_PORT = 1112
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create new socket
    address = (SERVER_ADDRESS, DEST_PORT)  # tuple with the connection information
    connection.connect(address)  # connect to server
    while True:
        message = input("Enter a command: ")
        connection.sendall(message.encode())  # send a message
        if message == "EXIT":  # IF USER ENTERED EXIT, EXIT THE LOOP --AFTER-- WE SENT THE EXIT COMMAND
            break
        server_response = connection.recv(4096)  # get server response
        server_response = server_response.decode()  # decode it
        print(server_response)  # print it
    connection.close()


if __name__ == '__main__':
    main()
