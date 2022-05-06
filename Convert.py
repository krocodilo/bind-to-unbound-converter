#!/usr/bin/python

from sys import argv, stdin
from os import path

#Missing - allow the two argument options to be independent. Because, for now, if you use a file, it will create pointers by default


def Convert(skippointers=True, file=False):
    if file:
	bindconfig = file
    else:
	print "\n\n\n\n//////////////////////////////////////////////////"
	print "            Please place your BIND host configuration below:\n\n"
	print "INPUT:\n--------------------------------------------"
	bindconfig = stdin.readlines()
	print "\n--------------------------------------------\n\n\n\n\n"

    print "OUTPUT:\n--------------------------------------------"

    for line in bindconfig:
	if line.strip() == "":
	    #check if it is an empty line
	    print line
	elif line.strip() != "" and line.strip()[0] == ';':
	    #check if it is a comment line
	    print '#' + line.strip()[1:]
	else:
	    line = line.strip().split()
	    comment = [s for s in line if ";" in s]

	    if comment:
		#If it found an inline comment, get the index of the first appearence:
		index = line.index(comment[0])

		hostname = line[0]
		if len(line[1:index-1]) == 1:
		    #If there is only one word for registers
		    register = "".join(line[1:index-1])
		elif len(line[1:index-1]) > 1:
		    #If there are more words for registers
		    register = " ".join(line[1:index-1])
		else:
		    #If there are no words between the hostname and the IP
		    print "\n\n    ERROR: There is no register on this line -  ", line

		ip = line[index-1]
                inlinecomment = "\t\t#" + " ".join(line[index:])[1:]	#To get the text only, without the BIND comment indicator (";")

	    else:
		#If there are no inline comments
		hostname = line[0]
                if len(line[1:-1]) == 1:
                    #If there is only one word for registers
                    register = "".join(line[1:-1])
                elif len(line[1:-index]) > 1:
                    #If there are more words for registers
                    register = " ".join(line[1:-1])
                else:
                    #If there are no words between the hostname and the IP
                    print "\n\n    ERROR: There is no register on this line -  ", line

		ip = line[-1]
		inlinecomment = ""

            print 'local-data: "' + hostname + '.itecons.pt.', '\t\t', register, '\t', ip + '"' + inlinecomment

	    if not skippointers and register != "CNAME":
		#This condition is successful by default.
		print 'local-data-ptr: "' + ip, hostname + '.itecons.pt' + '"'

    print "--------------------------------------------\n\n\n"


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
if __name__ == '__main__':
    try:
	print "\n\n\n    This program will convert DNS host register configuration from BIND to Unbound configuration. As input, insert only the hosts configuration. It will create a list of 'local-data' and 'local-data-ptr' entries."
	print "        > Use '-p' to skip the creation of pointers."
	print "        > Use '-f' to read from a file. You need to specify a valid file after this option."
	print "\n    If you're in doubt of what text to insert, take a look at the example file:   Example_BIND_Hosts_Configuration.txt\n\n"
        if len(argv) == 2 and argv[1] == '-p':
	    print "        FYI: You have chosen not to create pointers.\n\n"
	    Convert()
	elif len(argv) == 2 and argv[1] != '-p' and argv[1] != '-f':
	    print "\n\n\n    ERROR with arguments.\n\n\n"
	    exit
        elif len(argv) > 1 and argv[1] == '-f':
	    if len(argv) == 2 or len(argv) == 3 and not path.isfile(argv[2]):
		print "\n\n    >>> Please specify a valid file when you use '-f' option.\n\n\n"
		exit
	    else:
		#If the specified file exists:
		file = open(argv[2], "r")
		filecontent = file.readlines()
		file.close()
		Convert(False, filecontent)
	else:
	    #The default option
	    while True:
		Convert(False)


    except KeyboardInterrupt:
	print '\n\n\n \t\t\t <Terminated>\n\n\n'
	exit

    exit
