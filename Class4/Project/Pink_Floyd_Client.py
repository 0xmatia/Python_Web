import socket
import time
from termcolor import colored
import colorama

IP = "127.0.0.1"
PORT = 9011
colorama.init()  # make colors visible


def main():
    command_list = ["Alist", "SongsInAlb", "SongLen", "GetLyc", "WhichAlb", "SByName", "SByLyc", "Exit"]
    choice = "Alist"
    connection = connect_server(IP, PORT)  # obtain the connection socket
    while not choice == command_list[7]:
        print(
            colored(" >>>>>> Command list: Alist, SongsInAlb, SongLen, GetLyc, WhichAlb, SByName, SByLyc, Exit <<<<<<",
                    "magenta", attrs=['bold']))
        choice = input("Enter command: ")
        if choice == command_list[0]:
            connection = assemble_request(command_list[0], connection)
        elif choice == command_list[1]:
            album_name = input("Enter album name: ")
            connection = assemble_request(command_list[1], connection, album_name)
        elif choice == command_list[2]:
            song_name = input("Enter song name: ")
            connection = assemble_request(command_list[2], connection, song_name)
        elif choice == command_list[3]:
            song_name = input("Enter song name: ")
            connection = assemble_request(command_list[3], connection, song_name)
        elif choice == command_list[4]:
            song_name = input("Enter song name: ")
            connection = assemble_request(command_list[4], connection, song_name)
        elif choice == command_list[5]:
            word = input("Enter a word: ")
            connection = assemble_request(command_list[5], connection, word)
        elif choice == command_list[6]:
            word = input("Enter a word: ")
            connection = assemble_request(command_list[6], connection, word)
        elif choice == command_list[7]:
            assemble_request(command_list[7], connection)  # send exit request
        else:
            print(colored("Invalid command!\n", "red", attrs=['bold']))


def assemble_request(command, connection, parameter=""):
    """
    The function tries to send the request to server, throws exception if fails and tries to reconnect
    :param command: the command to send
    :type command: str
    :param connection: the connection socket
    :type connection: socket.py
    :param parameter: the parameters the user want to send to the server
    :type parameter: str
    :return: the socket - the same one if nothing fails, the updates socket if it reached the exception
    """
    request = ("command=" + command + "&parameter=" + parameter).encode()
    try:
        connection.sendall(request)
        print(colored(connection.recv(4096).decode(), "green"))
    except Exception:  # if you cannot connect to server, try to reconnect
        print("Re-connecting to server\n")
        return connect_server(IP, PORT)
    return connection


def connect_server(IP, PORT):
    """
    This function tries to connect to the server
    :param IP: The ip of the server
    :type IP: str
    :param PORT: the port the server is listening to
    :type PORT: int
    :return: the connection socket
    :rtype: socket
    """
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (IP, PORT)
    msg = ""
    while not msg == "Welcome to Pink Floyd database!":
        try:
            connection.connect(address)
            msg = connection.recv(1024).decode()
        except Exception:
            print("Can't reach server, trying again")
            time.sleep(2)
    print(msg)  # connection to server was successful
    return connection


if __name__ == '__main__':
    main()
