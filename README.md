Redirect the stderr in Python
=============================

I could overwrite the Python _sys.stderr_ to redirect it to _/dev/null_:
  
```
import sys
sys.stderr = open("/dev/null", 'w')
sys.stderr.write("nananana")
```

but this doesn't work if I load a library that prints to the _stderr_, because _sys.stderr_ has no control over the operations beyond the Python interpreter.

In such case, I can open a pipe and use `os.dup2` to copy it to the `stderr` file descriptor.

This works because the file descriptor is process-wide, and the file descritor substitutioon affects the loaded library as well.

Sample code
-----------

You can compile the simple module that prints a message to _stderr_ with

`gcc -shared -fpic -o clib.so clib.c`

and run the simple Python code that does the redirection with

`python main.py`

