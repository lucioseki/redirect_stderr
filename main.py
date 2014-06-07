#!/usr/bin/env python
import os
import sys
from ctypes import cdll

sys.stderr.write("this is printed to stderr first\n")

# backup of the stderr
fno_err = sys.stderr.fileno()
stderr = os.dup(fno_err)

# redirect the stderr to an open pipe
pipeout, pipein = os.pipe()
os.dup2(pipein, fno_err)

# this message will be redirected to the pipe
sys.stderr.write("this shouldn't be printed to stderr\n")

# The message that this loaded library prints to stderr
# will also be redirected to the pipe
lib = cdll.LoadLibrary("./clib.so")
lib.cfunc()

# Bring stderr back
os.dup2(stderr, fno_err)
sys.stderr.write("this is printed to stderr last\n\n")

print("Printing to stdout the messages redirected to the pipe:")
print(bytes.decode(os.read(pipeout, 128)))
