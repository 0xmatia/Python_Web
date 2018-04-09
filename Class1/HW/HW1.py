import requests
import time


def main():
    assemble_password()


def assemble_password():
    password = ""
    BASE_URL = "http://nahman.magshimail.com/files"
    number = 11
    file = "/file" + str(number) + ".nfo"
    while not (requests.get(BASE_URL + file).status_code == 404):
        time.sleep(1)
        file = "/file" + str(number) + ".nfo"
        password += requests.get(BASE_URL + file).text[99]
        number += 1
        print(password)


if __name__ == '__main__':
    main()
