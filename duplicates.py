import os
import sys


def are_files_duplicates(file_path):
    list_files = []
    for f_path, all_dirs, all_files in os.walk(file_path):
        for file_data in all_files:
            full_path = os.path.join(f_path, file_data)
            about_file = []
            file_dir = os.path.dirname(full_path)
            file_name = os.path.basename(full_path)
            file_size = os.path.getsize(full_path)
            for file_info in list_files:
                if (file_name == file_info[1] and file_size == file_info[2]):
                    print('Дубликат в папках:', file_info[0], 'и',
                          file_dir, '. Файл:', file_name, ',', file_size, 'b.')
                    break
            else:
                about_file.append(file_dir)
                about_file.append(file_name)
                about_file.append(file_size)
                list_files.append(about_file)

    return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help':
            print("Скрипт просматривает все файлы и ищет дубликаты в папке.")
            print("Дубликаты – это два файла с одинаковым именем и размером.")
            print("Введите в терминале: python3.5 dublicates.py your_path")
        else:
            if os.path.isdir(sys.argv[1]) is False:
                print("Указанная папка не обнаружена!")
            else:
                are_files_duplicates(sys.argv[1])
    else:
        print("Не задана папка для поиска дубликатов!")
