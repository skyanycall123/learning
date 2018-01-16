#usr/bin/python3
# coding = utf-8
# file name test

"""
Usage:
    test  <name>

Options:
    -h      help
"""

from docopt import docopt

if __name__ == '__main__':
    """command line """
    arguments = docopt(__doc__)
    print(arguments)
