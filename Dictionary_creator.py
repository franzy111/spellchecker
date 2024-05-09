import re


class DictionaryCreator:
    def __init__(self, file_name):
        self._file_name = file_name

    def create(self, path_to_save):
        """
        Создаёт словарь на основе полученного текста
        """
        pattern = re.compile("[,.?/…!\"\'*–—();:«»„“1234567890\\[\\]]")
        dictionary = dict()
        with open(self._file_name, "r", encoding="utf-8") as file:
            text = file.readlines()
            for line in text:
                for word in line.split():
                    clean_word = re.sub(pattern, "", word)
                    if clean_word != "":
                        if clean_word.lower() in dictionary:
                            dictionary[clean_word.lower()] += 1
                        elif clean_word in dictionary:
                            dictionary[clean_word] += 1
                        elif clean_word not in dictionary:
                            dictionary[clean_word] = 1
        with open(path_to_save, "w", encoding="utf-8") as file:
            for word, cost in sorted(dictionary.items(), key=lambda item: item[1], reverse=True):
                file.write(word + " " + str(cost) + "\n")


if __name__ == "__main__":
    dictionary_creator = DictionaryCreator("test_text.txt")
    print(dictionary_creator.create("dict.txt"))
