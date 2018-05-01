def get_text(file_path):
    with open(file_path, "r") as text_file:
        string = text_file.read().lower()
    return string


def init_count_dict(my_dict):
    char = 'a'
    for i in range(0, 26):
        my_dict[char] = 0
        char = ord(char) + 1


def count_letters_in_text(letter_dict, file):
    text = get_text(file)
    for char in text:
        if char.isalpha():
            letter_dict[char] += 1