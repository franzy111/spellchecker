import argparse
import SpellChecker


def main():
    parser = argparse.ArgumentParser(description="T9")

    parser.add_argument("text", type=str, help="Введите текст без знаков препинания")
    parser.add_argument("-n", "--number", type=int, default=float('inf'),
                        help="Введите количество первых ошибок для поиска (Чтобы найти все, оставьте поле пустым)")

    args = parser.parse_args()

    checker = SpellChecker.SpellChecker()
    correct = checker.spell_check(args.text, args.number)
    checker.print_result(correct, args.text)


if __name__ == "__main__":
    main()
