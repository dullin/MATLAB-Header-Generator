def create(fcn):
    #header = []
    #header.append('%{} - ONELINEDESCRIPTION\n'.format(fcn['name'].upper()))
    #header.append('%MOREDESCRIPTION\n')
    #header.append('%\n')

    #header.append('% Syntax: ')

    # Have to append each line individually if I want to add indent at the end
    header = ['%{} - ONELINEDESCRIPTION\n'.format(fcn['name'].upper()),
              '%MOREDESCRIPTION\n', '%\n',
              '% Syntax: ']
    if fcn['output'] is not None:
        header.append('[{}'.format(fcn['output'][0]))
        if len(fcn['output']) > 1:
            for outArg in fcn['output'][1:]:
                header.append(', {}'.format(outArg))
        header.append('] = ')
    header.append('{}'.format(fcn['name']))
    if fcn['input'] is not None:
        header.append('({}'.format(fcn['input'][0]))
        if len(fcn['output']) > 1:
            for inArg in fcn['input'][1:]:
                header.append(', {}'.format(inArg))
        header.append(')')
    header.append('\n')
    header.append('%\n')
    if fcn['input'] is not None:
        header.append('% Inputs:\n')
        header.append('%    {} [TYPE] - DESCRIPTION\n'.format(fcn['input'][0]))
        if len(fcn['input']) > 1:
            for outArg in fcn['input'][1:]:
                header.append('%    {} [TYPE] - DESCRIPTION\n'.format(outArg))
        header.append('%\n')

    if fcn['output'] is not None:
        header.append('% Outputs:\n')
        header.append('%    {} [TYPE] - DESCRIPTION\n'.format(fcn['output'][0]))
        if len(fcn['output']) > 1:
            for outArg in fcn['output'][1:]:
                header.append('%    {} [TYPE] - DESCRIPTION\n'.format(outArg))
        header.append('% \n')

    header.append('% Example:\n')
    header.append('%    EXAMPLE\n')
    header.append('%\n')
    header.append('% Other m-files: OTHER\n')
    header.append('%\n')
    header.append('% See also: OTHER_FUNCTION\n\n')

    header = ['{}{}'.format(' '*fcn['start_indent'],line) if line[0]=='%' else line for line in header ]
    return header


def insert(filelines, header, insert_line):
    while filelines[insert_line][0] == '%' or filelines[insert_line][0] == '\n':
        del filelines[insert_line]
    filelines[insert_line:insert_line] = header
    #print(filelines)
    return filelines


def insert_list(filelines, fcn_list):
    for function in reversed(fcn_list['functions']):
        header = create(function)
        filelines = insert(filelines, header, function['start_line'])
        #print(filelines)
    return filelines
    # fileout = open('testheader.m', 'w')
    # fileout.writelines(filelines)
    # fileout.close()


def insert_header(fcn_list):
    f = open(fcn_list['filename'])
    filelines = f.readlines()
    f.close()
    filelines = insert_list(filelines, fcn_list)
    f = open('finaltest.m', 'w')
    f.writelines(filelines)
    f.close()
