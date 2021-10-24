import os


# get all extentions of files that this directory have

def collect_extentions() -> set:
    extentions = set()
    current_path = os.getcwd()
    items = os.listdir(current_path)
    for item in items:
        ext = os.path.splitext(item)[1]
        if ext != '':  # for files like .git
            extentions.add(ext)
    return extentions
