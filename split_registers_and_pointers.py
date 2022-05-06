#!/usr/bin/python

from sys import argv, stdin
from os import path

def Split(file):
	registers = []
	pointers = []
	for line in file:
		if line[0] == '#':
			#If it is a 'big' comment
                        registers.append('\n\n' + line)
                        pointers.append('\n\n' + line)
		elif line.strip() and line.strip()[0] == '#':
			#If it is a 'small'comment
			registers.append('\n' + line)
                        pointers.append('\n' + line)
		elif line[:11] == 'local-data:':
			registers.append(line.strip())
		elif line[:15] == 'local-data-ptr:':
			pointers.append(line.strip())

	registers_filename = argv[1] + '_resgisters'
	pointers_filename = argv[1] + '_pointers'

	with open(registers_filename, 'w') as f:
		for line in registers:
			f.write(line + '\n')

        with open(pointers_filename, 'w') as f:
		for line in pointers:
	                f.write(line + '\n')


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
if __name__ == '__main__':
    try:
	print '\n\n\n'
        if len(argv) == 2 and not path.isfile(argv[1]):
            print "\n\n    >>> Please specify a valid file.\n\n\n"
	    exit
	else:
	    #If the specified file exists:
	    file = open(argv[1], "r")
	    filecontent = file.readlines()
	    file.close()
    	    Split(filecontent)

    except KeyboardInterrupt:
	print '\n\n\n \t\t\t <Terminated>\n\n\n'
	exit

    exit
