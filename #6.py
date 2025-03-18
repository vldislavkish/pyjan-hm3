def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    num_lines = content.count('\n')
    num_words = len(content.split())
    num_chars = len(content)

    result = (
        f"Статистика файла:\n"
        f"Количество строк: {num_lines}\n"
        f"Количество слов: {num_words}\n"
        f"Количество букв: {num_chars}\n"
    )
    print(result)

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(result)


process_file('test')
