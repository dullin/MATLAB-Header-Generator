from filelist import filelist


def functionlist(file_path):
    with open(file_path) as fp:
        file_lines = fp.read().splitlines()
    return [(line, index) for index,line in enumerate(file_lines) if line.split(' ', 1)[0] == 'function']


def list_functionlist(list_file_path):
    return [(file_path, functionlist(file_path))for file_path in list_file_path]


if __name__ == "__main__":
    list = list_functionlist(filelist('/home/dullin/dev/files'))
    print(list)