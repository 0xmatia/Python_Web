import socket
import Databaser
import sys

def main():
    print(sys.path)
    PORT = 9011
    print("Listening on port 9011")
    print(Databaser.extract_data("Pink_Floyd_DB.txt"))
    call_function = {"Alist": Alist, "SongsInAlb": SongsInAlb, "SongLen": SongLen, "GetLyc": GetLyc,
                     "WhichAlb": WhichAlb, "SByName": SByName, "SByLyc": SByLyc}
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', PORT)
    listen_socket.bind(server_address)

    while True:  # the server runs forever, never closes. the second while is for the client socket, which closes
        listen_socket.listen(1)
        client_socket, client_address = listen_socket.accept()
        command = ""
        client_socket.sendall("Welcome to Pink Floyd database!".encode())
        while not command == "Exit":
            try:  # try to send response, throw exception if you can't
                response = client_socket.recv(1024).decode()
                command, parameter = disassemble_response(response)
                if not command == "Exit":
                    a = call_function[command](parameter)
                    client_socket.sendall(a.encode())
            except Exception:
                print("Client disconnected unexpectedly")
                break
        client_socket.close()
        print("Connection closed. Listening on port 9011")
    listen_socket.close()


def disassemble_response(client_response):
    """
    The function disassembles the request to command and parameter
    :param client_response:the response of the clients
    :type client_response: str
    :return:command the parameter
    :rtype: tuple
    """
    command = client_response[8:client_response.index('&')]
    parameter = client_response[client_response.index('&') + 11:]
    return command, parameter


def Alist(parameter):
    print("Alist function activated")
    return "Alist function activated"


def SongsInAlb(paramter):
    print("SongsInAlb function activated")
    return "SongsInAlb function activated"


def SongLen(parameter):
    print("SongsLen function activated")
    return "SongsLen function activated"


def GetLyc(parameter):
    print("GetLyc function activated")
    return "GetLyc function activated"


def WhichAlb(parameter):
    print("WhichAlb function activated")
    return "WhichAlb function activated"


def SByName(parameter):
    print("SByName function activated")
    return "SByName function activated"


def SByLyc(parameter):
    print("SByLyc function activated")
    return "SByLyc function activated"


if __name__ == '__main__':
    main()
