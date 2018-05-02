import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # make the socket global


def main():
    IP = "127.0.0.1"
    PORT = 9011
    command_list = ["Alist", "SongsInAlb", "SongLen", "GetLyc", "WhichAlb", "SByName", "SByLyc", "Exit"]
    address = (IP, PORT)
    connection.connect(address)
    print(connection.recv(1024).decode())  # connection to server was successful
    choice = "Alist"
    while not choice == command_list[7]:
        print(" >>>>>>Command list: Alist, SongsInAlb, SongLen, GetLyc, WhichAlb, SByName, SByLyc, Exit<<<<<<")
        choice = input("Enter command: ")
        if choice == command_list[0]:
            assemble_request(command_list[0])
        elif choice == command_list[1]:
            album_name = input("Enter album name: ")
            assemble_request(command_list[1], album_name)
        elif choice == command_list[2]:
            song_name = input("Enter song name: ")
            assemble_request(command_list[2], song_name)
        elif choice == command_list[3]:
            song_name = input("Enter song name: ")
            assemble_request(command_list[3], song_name)
        elif choice == command_list[4]:
            song_name = input("Enter song name: ")
            assemble_request(command_list[4], song_name)
        elif choice == command_list[5]:
            word = input("Enter a word: ")
            assemble_request(command_list[5], word)
        elif choice == command_list[6]:
            word = input("Enter a word: ")
            assemble_request(command_list[6], word)


def assemble_request(command, parameter=""):
    #  print(("command=" + command + "&parameter=" + parameter).encode())
    connection.sendall(("command=" + command + "&parameter=" + parameter).encode())


if __name__ == '__main__':
    main()
