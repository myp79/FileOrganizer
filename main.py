import os


# get all extentions of files that this directory have

def collect_extentions() -> set:
    extentions = set()
    current_path = os.getcwd()
    items = os.listdir(current_path)
    for item in items:
        ext = os.path.splitext(item)[1]
        if ext != '':  # for files like .git
            extentions.add(ext[1:])
    return extentions


def make_directory(ext: set) -> set:
    # make directories of extention and ready for move files
    current_path = os.getcwd()
    directory_path = set()
    for item in ext:
        try:  # if directory exist
            path = os.path.join(current_path, item)
            os.mkdir(path)
            directory_path.add(path)
        except OSError as error:
            print(error)
    return directory_path
