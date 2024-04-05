import os
import pytest


def count_words_and_sentences(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            sentence_endings = "...!?."

            # Підраховуємо слова
            words = content.split()
            num_words = len(words)

            # Підраховуємо речення
            num_sentences = 0
            for char in content:
                if char in sentence_endings:
                    num_sentences += 1

            # Перевіряємо, чи останнє речення закінчується на символи-роздільники
            if not content.endswith(tuple(sentence_endings)):
                num_sentences += 1

            if content == '':
                num_sentences, num_words = 0, 0

            return num_words, num_sentences
    except FileNotFoundError:
        ex_msg = "Файл не знайдено"
        return ex_msg
    except Exception as e:
        print("Сталася помилка:", e)


if __name__ == "__main__":
    pytest.main()
