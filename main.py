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


# Функція для створення тимчасового текстового файлу з вмістом для тестування
def create_temp_file(content):
    temp_file_path = 'temp_test_file.txt'
    with open(temp_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    return temp_file_path


def test_with_sentences_ok():
    # Тестування, коли файл існує і має вміст
    content = "Це тестовий рядок. Це також! І знову."
    temp_file_path = create_temp_file(content)
    num_words, num_sentences = count_words_and_sentences(temp_file_path)
    assert num_words == 7
    assert num_sentences == 3
    os.remove(temp_file_path)


def test_with_empty_file_ok():
    # Тестування, коли файл існує, але порожній
    temp_file_path = create_temp_file('')
    num_words, num_sentences = count_words_and_sentences(temp_file_path)
    assert num_words == 0
    assert num_sentences == 0
    os.remove(temp_file_path)


def test_with_nonexistent_file_exception():
    # Тестування, коли файл не існує
    ex_msg = count_words_and_sentences('nonexistent_file.txt')
    assert ex_msg == "Файл не знайдено"


def test_with_separators_ok():
    # Тестування, коли вміст файлу містить розділювачі
    content = "Слово1, слово2; слово3: слово4 слово5"
    temp_file_path = create_temp_file(content)
    num_words, num_sentences = count_words_and_sentences(temp_file_path)
    assert num_words == 5
    assert num_sentences == 1
    os.remove(temp_file_path)


if __name__ == "__main__":
    pytest.main()
