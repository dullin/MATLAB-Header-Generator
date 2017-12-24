from os import walk


def filelist(path):
    path_list = []
    for (dirpath, dirnames, filenames) in walk(path):
        for file in filenames:
            if file.endswith('.m'):
                path_list.append(dirpath + '/' + file)
    return path_list


if __name__ == "__main__":
    print(filelist('/home/dullin/dev/files'))
    print('Test done')
