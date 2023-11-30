#!/usr/bin/python3

if __name__ == "__main__":
    """Do Nothing, relax and Exit, You don try"""

    import sys

    argv = sys.argv[1:]
    len = len(argv)

    if len == 0:
        print("{0} arguments.".format(len))

    elif len == 1:
        print("{0} argument:".format(len))

    else:
        print("{0} arguments:".format(len))
        
    for i, arg in enumerate(argv):
        print("{0}: {1}".format(i + 1, argv[i]))
