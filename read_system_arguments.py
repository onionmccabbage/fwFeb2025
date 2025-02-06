# Every time we run a python module it ALWAYS receives system arguments
import sys

# the zeroeth member of sys.argv is ALWAYS the module name
if len(sys.argv)>1:
    for i in sys.argv[1:]:
        print( i )