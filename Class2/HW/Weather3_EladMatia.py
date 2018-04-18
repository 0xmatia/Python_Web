import socket
import datetime


def main():
    # get hold of the text data
    path = "C:\\Users\\eladm\\Documents\\Python_Web\\Class2\\HW\\capitals20.txt"
    IP = '52.89.157.137'
    PORT = 77
    address = (IP, PORT)
    word_list = []
    with open(path, 'r') as file:
        word_list = file.read().split('\n')
    temp_date = str((datetime.date.today()))  # assemble date
    date = temp_date[8] + temp_date[9] + "/" + temp_date[5] + temp_date[6] + "/" + temp_date[:4]
    global_list = []
    for i in range(20):
        main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        main_socket.connect(address)
        server_response = main_socket.recv(1024)

        current_line = word_list[i].split(',')
        current_city = current_line[1] + ", " + current_line[2]
        request = "100:REQUEST:city=" + current_city + "&date=" + date + "&checksum=" + build_checksum(current_city,
                                                                                                       date)
        # send adn receive data
        main_socket.sendall(request.encode())
        server_response = main_socket.recv(1024)
        server_response = server_response.decode()
        if not int(server_response[0:3]) == 500:
            temp = server_response[
                   server_response.find("temp=") + len("temp="):server_response.find("temp=") + len("temp=") + 4]
            global_list.append((current_city, temp))
    # sort:
    global_list.sort(key=return_second, reverse=True)
    j = 1
    for i in global_list:
        city = i[0]
        city = city.split(',')[1]
        print(str(j)+". " + i[1] + " degrees, "+city)
        j += 1


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
    temp = int(date[0]) + int(date[1]) + int(date[3]) + int(date[4]) + int(date[6]) + int(date[7]) + int(date[8]) + int(
        date[9])
    checksum += str(temp)
    return checksum


def return_second(temp_tuple):
    """
    Return the second element of tuple
    :param temp_tuple: the tuple
    :type temp_tuple: tuple
    :return: The second element of the given tuple
    :rtype: float
    """
    return float(temp_tuple[1])


if __name__ == '__main__':
    main()
