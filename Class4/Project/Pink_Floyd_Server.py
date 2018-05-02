import socket


def main():
    PORT = 9011
    print("Listening on port 9011")
    call_function = {"Alist": Alist, "SongsInAlb": SongsInAlb, "SongLen": SongLen, "GetLyc": GetLyc, "SByName": SByName,
                     "SByLyc": SByLyc}
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', PORT)
    listen_socket.bind(server_address)
    listen_socket.listen(1)
    client_socket, client_address = listen_socket.accept()
    command = ""
    while not command == "EXIT":
        print("Loop")
        client_socket.sendall("Welcome to Pink Floyd database!".encode())
        response = client_socket.recv(1024).decode()
        command, parameter = disassemble_response(response)
        call_function[command](parameter)
    client_socket.close()
    listen_socket.close()


def disassemble_response(client_response):
    command = client_response[8:client_response.index('&')]
    parameter = client_response[client_response.index('&') + 11:]
    return command, parameter


def Alist(parameter):
    print("Alist function activated")


def SongsInAlb(paramter):
    print("SongsInAlb function activated")


def SongLen(parameter):
    print("SongsLen function activated")


def GetLyc(parameter):
    print("GetLyc function activated")


def WhichAlb(parameter):
    print("WhichAlb function activated")


def SByName(parameter):
    print("SByName function activated")


def SByLyc(parameter):
    print("SByLyc function activated")


if __name__ == '__main__':
    main()
