from math import log


class SpellChecker:
    def __init__(self, path="dict.txt"):
        with open(path, "r", encoding="utf-8") as file:
            self.words = [word.split()[0] for word in file.readlines()]
            self.word_cost = dict((word, log((i + 1) * log(len(self.words)))) for i, word in enumerate(self.words))
            self.the_longest = max(len(x) for x in self.words)
            self.len_dict = dict([(i, []) for i in range(1, self.the_longest + 1)])
            for word in self.words:
                self.len_dict[len(word)].append(word)

    @staticmethod
    def levenstein(str_1, str_2):
        """
        Считает расстояние Левенштейна двух слов
        """
        n, m = len(str_1), len(str_2)
        if n > m:
            str_1, str_2 = str_2, str_1
            n, m = m, n

        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if str_1[j - 1] != str_2[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        return current_row[n]

    def checking_gaps(self, word):
        """
        Проверка на лишние пробелы
        :param word: слово
        :return: исправленное слово
        Источник: stackoverflow.com/questions/47730524/spell-check-and-return-the-corrected-term-in-python
        """

        # Find the best match for the i first characters, assuming cost has
        # been built for the i-1 first characters.
        # Returns a pair (match_cost, match_length).
        def best_match(i):
            candidates = enumerate(reversed(cost[max(0, i - self.the_longest):i]))
            return min((c + self.word_cost.get(word[i - k - 1:i], 9e999), k + 1) for k, c in candidates)

        # Build the cost array.
        cost = [0]
        for i in range(1, len(word) + 1):
            c, k = best_match(i)
            cost.append(c)

        # Backtrack to recover the minimal-cost string.
        out = []
        i = len(word)
        while i > 0:
            c, k = best_match(i)
            assert c == cost[i]
            out.append(word[i - k:i])
            i -= k

        return " ".join(reversed(out))

    def checking_for_hyphens(self, word):
        """
        Проверка на лишний дефис
        :param word: проверяемое слово
        :return: True, если есть лишний дефис, иначе False
        """

        new_words = word.split("-")
        for new_word in new_words:
            if new_word not in self.words:
                return False
        return True

    @staticmethod
    def fancy_print(new, old, found_all):
        """
        Вывод результата
        :param new: Исправленное слово
        :param old: Изначальное слово
        :param found_all: Булевский массив, который хранит True, если слово изначально написано корректно,
        и хранит False, если слова нет в словаре, но подобрать замену ему не удалось
        :return: Печатает в консоль результат спеллчекинга
        """

        print("Исходная строка: " + " ".join(old))
        print("Результат: " + " ".join(new))
        for i in range(len(new)):
            if new[i] != old[i]:
                print(old[i] + " -> " + new[i])
            elif not found_all[i]:
                print(old[i] + " -> " + "(Не удалось подобрать корректное слово)")

    def spell_check(self, s, num=9e999):
        """Исправление первых num орфографических ошибок в строке s"""

        correct = s.split()
        first_version = s.split()
        found_all = [True] * len(correct)
        for i in range(len(correct)):
            found = False
            word = correct[i]
            if word in self.words:
                continue

            length = len(word)
            possible_length = [length, min(length + 1, self.the_longest), max(length - 1, 1),
                               min(length + 2, self.the_longest), max(length - 2, 1)]
            possible = ""
            for j in possible_length:
                for candidate in self.len_dict[j]:
                    dist = self.levenstein(word, candidate)
                    if dist == 1:
                        correct[i] = candidate
                        num -= 1
                        found = True
                        break
                    elif dist == 2 and possible == "":
                        possible = candidate
                        continue
                if found:
                    break
            if not found:
                if possible:
                    correct[i] = possible
                    num -= 1
                elif self.checking_for_hyphens(correct[i]):
                    correct[i] = correct[i].replace("-", " ")
                else:
                    correct[i] = self.checking_gaps(correct[i])
                    for new_w in correct[i].split():
                        if new_w not in self.words:
                            correct[i] = first_version[i]
                            found_all[i] = False
            if num == 0:
                break
        self.fancy_print(correct, first_version, found_all)
        return " ".join(correct)


if __name__ == "__main__":
    spl = SpellChecker()
    print(spl.words)
