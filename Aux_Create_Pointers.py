#!/usr/bin/python

import sys
from subprocess import Popen, PIPE


def Create_Pointers(textarray=False):
    if textarray is False:
        print "\n\n\n\n//////////////////////////////////////////////////"
        print "            Please place your text below:\n\n"
        print "--------------------------------------------"
        textarray = sys.stdin.readlines()
        print "\n--------------------------------------------\n\n\n\n\n"

    for line in textarray:
	line = line.rstrip()
        if "local-data:" == line.lstrip()[:11]:
	    line = line
	    cmd1 = "echo '" + line + "' | cut -d'" + '"' + "' -f2 | cut -d' ' -f1"
	    cmd2 = "echo '" + line + "' | cut -d'" + '"' + "' -f2 | tr -s ' ' ' ' | cut -d' ' -f4"

	    hostname = Popen(cmd1, shell=True, stdout=PIPE).stdout.read()
	    ip = Popen(cmd2, shell=True, stdout=PIPE).stdout.read()

	    print line
	    print 'local-data-ptr: "' + ip.rstrip(),  hostname.rstrip()[0:-1] + '"\n'
	else:

	    print line.strip()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

if __name__ == '__main__':
    try:
        print "\n\n\n    This program is used only for creating pointers to host configuration in Unbound DNS Service. As input, it accepts configuration from unbound and parses each line that starts with 'local-data:'"
        Create_Pointers()
        exit
    except KeyboardInterrupt:
	print "\n\n \t\t\t\t<Terminated>\n\n"
	exit
