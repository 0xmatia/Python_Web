import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # make the socket global


def main():
    IP = "127.0.0.1"
    PORT = 9011
    flag = True
    command_list = ["Alist", "SongsInAlb", "SongLen", "GetLyc", "WhichAlb", "SByName", "SByLyc", "Exit"]
    address = (IP, PORT)
    connection.connect(address)
    print(connection.recv(1024).decode())  # connection to server was successful
    choice = "Alist"
    while not choice == command_list[7] and flag:
        print(" >>>>>>Command list: Alist, SongsInAlb, SongLen, GetLyc, WhichAlb, SByName, SByLyc, Exit<<<<<<")
        choice = input("Enter command: ")
        if choice == command_list[0]:
            flag = assemble_request(command_list[0])
        elif choice == command_list[1]:
            album_name = input("Enter album name: ")
            flag = assemble_request(command_list[1], album_name)
        elif choice == command_list[2]:
            song_name = input("Enter song name: ")
            flag = assemble_request(command_list[2], song_name)
        elif choice == command_list[3]:
            song_name = input("Enter song name: ")
            flag = assemble_request(command_list[3], song_name)
        elif choice == command_list[4]:
            song_name = input("Enter song name: ")
            flag = assemble_request(command_list[4], song_name)
        elif choice == command_list[5]:
            word = input("Enter a word: ")
            flag = assemble_request(command_list[5], word)
        elif choice == command_list[6]:
            word = input("Enter a word: ")
            flag = assemble_request(command_list[6], word)
    #  send exit request
    assemble_request(command_list[7])


def assemble_request(command, parameter=""):
    """
    The function tries to send request to server and throws exception if failes
    :param command: The command the user asked
    :type command: str
    :param parameter: the parameter required, empty by default
    :type parameter: str
    :return:False if the program failed to contact server
    :rtype: bool
    """
    try:
        connection.sendall(("command=" + command + "&parameter=" + parameter).encode())
        return True
    except Exception:
        print("Can't reach server. Program is being terminated.")
        return False


if __name__ == '__main__':
    main()
