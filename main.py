import os
import shutil


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


def make_directory(ext: str) -> os.path:
    # make directory of extention and ready for move files
    current_path = os.getcwd()
    try:  # if directory exist
        path = os.path.join(current_path, ext)
        os.mkdir(path)
        return path
    except OSError as error:
        print(error)


def move_file(ext: set) -> str:
    # move all same file to a type directory
    for item in ext:
        destination_path = make_directory(item)
        for file in os.listdir():
            if file.endswith(".%s" % item) and file != 'main.py':  # for not move script
                current_path = os.getcwd()
                shutil.move(os.path.join(current_path, file),
                            os.path.join(destination_path, file))
        yield 'Move .%s files done successfully' % item


if __name__ == '__main__':
    extentions = collect_extentions()
    for operation in move_file(extentions):
        print(operation)
