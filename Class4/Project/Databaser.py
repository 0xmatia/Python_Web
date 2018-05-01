def get_text(file_path):
    """
    The file returns the context of a given the file
    :param file_path: the file path
    :type file_path: str
    :return: the file context
    :rtype: str
    """
    with open(file_path, "r") as file:
        text_string = file.read()
    return text_string


def return_list_index(string, char):
    """
    The function returns a list with all the indexes of @param char
    :param string: the string to check occurrences
    :type string: str
    :param char: the char to search in the string
    :type char: string
    :return: a list with all the indexes of the string
    :rtype: list
    """
    index_list = []
    for i in string:
        if i == char:
            index_list.append(i+1)
    return index_list


def extract_data(filepath):
    song_list = []
    raw_string = get_text(filepath)
    # get song name:
    songs_name = return_list_index(raw_string, '*')
    print(songs_name)
    for i in songs_name:
        i = songs_name[i:raw_string.find(':', i)]
        print(i)


def main():
    extract_data("Pink_Floyd_DB.txt")


if __name__ == '__main__':
    main()