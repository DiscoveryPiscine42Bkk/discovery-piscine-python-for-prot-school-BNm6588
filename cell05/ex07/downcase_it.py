#!/usr/bin/env python3
import sys

# Check if exactly one argument is passed (excluding the script name itself)
if len(sys.argv) != 2:
    print("none")
else:
    # Print the argument in lowercase
    print(sys.argv[1].lower())
