import socket


def main():
    IP = "52.89.157.137"
    PORT = 77
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (IP, PORT)
    main_socket.connect(address)
    server_response = main_socket.recv(1024)  # get rid off the greeting message
    city = input("Enter city name (as City,  State): ")
    date = input("Enter date (DD/MM/YYYY): ")
    request = ("100:REQUEST:city=" + city + "&date=" + date + "&checksum=" + build_checksum(city, date))
    main_socket.sendall(request.encode())
    server_response = main_socket.recv(1024)
    server_response = server_response.decode()
    if int(server_response[0:3]) == 200:
        print("Temp = " + server_response[server_response.find("temp=")+len("temp="):server_response.find("temp=")+len("temp=")+5])
        print("Description: " + server_response[len("text=")+server_response.find("text="):])
    elif int(server_response[0:3]) == 500:
        print("Failure: " + server_response)


def build_checksum(city, date):
    """
    THe function build the checksum required for the weather app
    :param city: The city the user entered
    :type city: str
    :param date: date the user entered
    :type date: str
    :return: The checksum
    :rtype: str
    """
    # constants:
    LOWER_A = 'a'
    LOWER_z = 'z'
    CAPITAL_A = 'A'
    CAPITAL_Z = 'Z'
    checksum = 0
    # part one: sum the city chars
    for char in city:
        if (char.isalpha()) and (char <= LOWER_z) and (char >= LOWER_A):
            checksum += ord(char) - 97 + 1
        elif (char.isalpha()) and (char <= CAPITAL_Z) and (char >= CAPITAL_A):
            checksum += ord(char) - 65 + 1
    # now part two:
    checksum = str(checksum)
    checksum += '.'  # add a dot and go to the second part
    temp = int(date[0]) + int(date[1]) + int(date[3]) + int(date[4]) + int(date[6]) + int(date[7]) + int(date[8]) + int(date[9])
    checksum += str(temp)
    return checksum


if __name__ == '__main__':
    main()
