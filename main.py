from filelist import filelist
from function_parser import parse
from create_header import insert_header
import json



if __name__ == '__main__':
    singlefilename = '/home/dullin/dev/pythonparser/files/fcn1.m'
    fcn_single = parse(singlefilename)
    #print(filelist('/home/dullin/dev/files'))
    list_fcn = []
    list_file = filelist('/home/dullin/dev/pythonparser/files')
    for filename in list_file:
        list_fcn.append(parse(filename))
        #print(filename)

    #print(list_fcn)
    f = open('fcn_names.json', 'w')
    f.write(json.dumps(list_fcn, sort_keys=True, indent=4, separators=(',', ': ')))
    f.close()
    #header = create(fcn_single['functions'][0])
    #print(header)
    #insert(singlefilename,header,fcn_single['functions'][0]['start_line'])
    f = open('/home/dullin/dev/pythonparser/files/fcn1.m','r')
    testlines = f.readlines()
    insert_header(list_fcn[1])