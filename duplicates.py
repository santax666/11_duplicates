import os
import sys
import argparse

def get_all_files(path):
    all_files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            all_files.append(full_path)
    return all_files


def are_files_duplicates(files):
    list_files = {}
    dubl_files = {}
    for filename in files:
        file_info = (os.path.basename(filename), os.path.getsize(filename))
        if not file_info in list_files.keys():
            list_files[file_info] = os.path.dirname(filename)
        else:
            dubl_files[file_info] = os.path.dirname(filename)
    return dubl_files


def check_folder(path):
    return os.path.isdir(path)

def createParser():
    parser = argparse.ArgumentParser(usage='%(prog)s [аргументы]',
                                     description="Поиск дубликатов в" \
                                     "папке с помощью %(prog)s")
    parser._positionals.title = 'Обязательные аргументы'
    parser._optionals.title = 'Дополнительные аргументы'
    parser._actions[0].help = 'Показать эту справку и выйти.'
    parser.add_argument("dirpath", help="Путь к папке")
    return parser


if __name__ == '__main__':

    parser = createParser()
    namespace = parser.parse_args()
    dir_path = namespace.dirpath

    if check_folder(dir_path):
        all_files = get_all_files(dir_path)
        all_dubles = are_files_duplicates(all_files)
        if not len(all_dubles) == 0:
            for dubl_file in all_dubles:
                print(dubl_file,"- дубликат в папке:",
                                            all_dubles.get(dubl_file))
        else:
            print("Дубликаты в папке","не найдены")
    else:
        print("Указанная папка не обнаружена!")
