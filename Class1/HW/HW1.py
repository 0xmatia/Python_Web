import requests
import time


def main():
    assemble_password()
    # ANSWER: Armadillo_is_the_best*#*


def assemble_password():
    """
    The function assembles the password for the challenge and print it
    :return: None
    """
    password = ""
    BASE_URL = "http://nahman.magshimail.com/files"
    number = 11
    file = "/file" + str(number) + ".nfo"
    while not (requests.get(BASE_URL + file).status_code == 404):  # until no file is found
        time.sleep(1)
        file = "/file" + str(number) + ".nfo"
        password += requests.get(BASE_URL + file).text[99]  # assembles the password
        number += 1
    print(password[:-1])  # don't use the last character of the 404 page


if __name__ == '__main__':
    main()
