import os


def are_files_duplicates(file_path1, file_path_2):
    pass


def get_all_files(path):
    tuple_path_files = ()
    about_file = ()
    for files_and_folders in os.listdir(path):
        full_path = os.path.join(path, files_and_folders)
        if os.path.isfile(full_path):
            about_file.append(os.path.dirname(full_path))
            about_file.append(files_and_folders)
            about_file.append(os.path.getsize(full_path))
            tuple_path_files.append(about_file)
            about_file.clear()
        else:
            get_all_files(full_path)
    return tuple_path_files

if __name__ == '__main__':
    pass

print(get_all_files("/home/kodi/python"))
