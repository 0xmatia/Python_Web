import requests


def main():
    get_common_words()
    # ANSWER: and now for something completely different


def get_common_words():
    """
    The function finds the secret password and print it
    :return: None
    :rtype: None
    """
    URL = "http://nahman.magshimail.com/final_phase/words.txt"
    word_list = requests.get(URL).text.split()
    uniques = []
    counts = []
    password = ""
    for word in word_list:  # creates a list with the unique words
        if word not in uniques:
            uniques.append(word)
    uniques.sort()
    for unique in uniques:
        counts.append((unique, word_list.count(unique)))
    counts.sort(key=return_second)  # sort it by the counts
    counts.reverse()  # from the bigger number to the lowest
    for i in range(6):  # print the 6 most used words
        word, count = counts[i]
        password = password + word + " "
    print(password[:-1])


def return_second(couple):
    """
    The function returns the second element of the tuple
    :param couple:
    :type couple:tuple
    :return: the second element of the tuple
    :rtype: int
    """
    return couple[1]


if __name__ == '__main__':
    main()
