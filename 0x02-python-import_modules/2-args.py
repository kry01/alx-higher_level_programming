#!/usr/bin/python3

import sys
argv = sys.argv
argc = len(argv)
if argc == 2:
    print("{} argument:".format(argc - 1))
else:
    print("{} arguments:".format(argc - 1))
for i in range(1, argc):
    print("{}: {}".format(i, argv[i]))
