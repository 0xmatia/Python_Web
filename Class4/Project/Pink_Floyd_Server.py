import socket
import Databaser

database = Databaser.extract_data("Pink_Floyd_DB.txt")
PORT = 9011


def main():
    print("Listening on port 9011")
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
        print(client_address[0] + " has connected on port " + str(client_address[1]))
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
    """
    the function returns a list with all the albums
    :param parameter: default empty parameter
    :type parameter: str
    :return: a list with album names
    :rtype: list
    """
    album_list = []
    print("Alist function is being activated")
    for song in database:
        if song[4] not in album_list:
            album_list.append(song[4])
    return "Album list: " + str(album_list)


def SongsInAlb(parameter):
    print("SongsInAlb function activated")
    # song[0] - song name, song[4] - album name
    song_list = []
    for song in database:
        if (song[4] == parameter) and (song[0] not in song_list):
            song_list.append(song[0])
    return "Songs in \'" + str(parameter) + '\': ' + str(song_list)


def SongLen(parameter):
    print("SongLen function activated")
    # song[0] - song name, song[2] - length
    for song in database:
        if song[0] == parameter:
            return parameter + "\'s length: " + str(song[2])


def GetLyc(parameter):
    """
    The function returns the lyrics for specific song
    :param parameter: song name
    :type parameter: str
    :return: the lyrics for the song
    :rtype: str
    """
    print("GetLyc function activated")
    # song[3] = lyrics, song[0] - song name
    for song in database:
        if song[0] == parameter:
            return "----Lyrics for \'" + song[0] + "\' are:----\n" + song[3]
    return "The entered song wasn't found"


def WhichAlb(parameter):
    """
    The function receives a song name and returns its album
    :param parameter: the song name
    :type parameter: str
    :return: the album of the song
    :rtype: str
    """
    print("WhichAlb function activated")
    # song[0] - song name, song[4] - album name
    for song in database:
        if song[0] == parameter:
            return "The song of \'" + song[0] + "\' is in the " + song[4] + "album"
    return "The entered song wasn't found"


def SByName(parameter):
    print("SByName function activated")
    song_list = []
    for song in database:
        if parameter.lower() in song[0].lower():
            song_list.append(song[0])
    return "Songs with the word you entered are in their name are: " + str(song_list) + "\n"


def SByLyc(parameter):
    print("SByLyc function activated")
    song_list = []
    for song in database:
        if parameter.lower() in song[3].lower():
            song_list.append(song[0])
    return "Songs with the lyrics you entered are: " + str(song_list) + "\n"


def cmnWords():
    words_list = []
    for album in database:
        for song in album:
            for lyc in song:


if __name__ == '__main__':
    main()
