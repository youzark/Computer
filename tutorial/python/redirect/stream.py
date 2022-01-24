#!/usr/bin/env python
import sys

## standard in
message = sys.stdin.read()
print(message)

print("this goes to standard out")

sys.stdout.write("this is also going to stdout \n")

print('this goes to stderr',file=sys.stderr)
sys.stderr.write("this is also going to stderr \n")
