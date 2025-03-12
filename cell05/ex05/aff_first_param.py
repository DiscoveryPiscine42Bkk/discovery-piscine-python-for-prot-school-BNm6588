#!/usr/bin/env python3
import sys

# Check if there are any command-line arguments
if len(sys.argv) > 1:
    # Print the first argument (excluding the script name itself)
    print(sys.argv[1])
else:
    # If no arguments, print 'none'
    print('none')
