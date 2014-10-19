Most-Recently-Accessed-File
===========================
Last Accessed File
=========================

-  Write a brief program in one of the above programming languages that, given a list of file names, will display the name of the mostly recently accessed file.  For example, if /tmp/a was the most recently accessed file, then

  - $ program /tmp/a /tmp/b /tmp/c
  - /tmp/a

  would be correctly formatted invocation and output.  In a comment at the top of the file, please explain the conditions under which your program might fail.

- Provide an equivalent implementation of #1 in any other programming language you like.  In this program's comments, please explain any different limitations that apply to this implementation from that in #1.

Implementations
---------------

I've provided two implementations as requested. The first uses Python, and the second uses Javascript.


### Running the Python version

```
./last_access.py b.txt a.txt c.txt
```

The output is:

```
b.txt
```

Comments-
1)	Script takes a list of filenames as arguments.
2)	An error message is printed if the path to the file is not found.
3)	An error message is printed to handle anything that is not a file.
4)	It also assumes that spaces for the files have been escaped.


### Running the javascript version

```
./last_access.js b.txt a.txt c.txt
```

The output is:

```
b.txt
```

Comments-
1)	Script takes a list of filenames as arguments.
2)	An error message is printed if the path to the file is not found.
3)	An error message is printed to handle anything that is not a file.
4)	It also assumes that spaces for the files have been escaped.
