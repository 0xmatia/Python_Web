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


def extract_data(input_file):
    song_index = 1
    song_name = ""
    song_length = 0
    singer = ""
    lyc = ""
    for song in range(0,
                      input_file.count(
                          "*")):  # run through the number of songs, each time assemble the required information

        # find song name
        song_index = input_file.find('*', song_index + 1)  # update the song index to the last appearance of *
        song_name = input_file[song_index + 1:input_file.find(':', song_index)]  # assign the song and go on!
        #  find song length
        singer_index = input_file.find(':', song_index) + 2
        singer = input_file[singer_index:input_file.find(":", singer_index)]
        # find song length
        length_index = input_file.find(':', singer_index) + 2
        song_length = input_file[length_index:input_file.find(":", length_index) + 3]
        # find song lyrics
        lyc_index = input_file.find(':', length_index) + 5
        lyc = input_file[lyc_index:input_file.find("*", length_index) or input_file.find("#", length_index)]


def main():
    extract_data(get_text("Pink_Floyd_DB.txt"))


if __name__ == '__main__':
    main()
