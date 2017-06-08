<a href="README.md"><img src="PicsForChapters/0_Start_filled.png" height="40"></a><a href="1_Short_Introduction.md"><img src="PicsForChapters/1_A_Short_Introduction_transparent.png" height="40"></a><a href="2_Install_Python.md"><img src="PicsForChapters/2_Install_Python.png" height="40"></a><a href="3_Time_to_Say_Goodbye.md"><img src="PicsForChapters/3_Time_to_Say_Goodbye.png" height="40"></a><a href="4_Advanced_Concepts.md"><img src="PicsForChapters/4_Advanced_Concepts.png" height="40"></a>


# A short introduction
## What is Python, and what is it not
Python is a programming language. Basically, a programming language is a set of instructions to tell the PC to do something. Every programming language has it's own grammar. And they are only theoretical constructs. You can not write software just with the language definition of python.

So obviously, you need some more stuff to get a programming language to do work. First of all, PCs don't understand text, they understand zeros and ones. So everything you have written, must be interpreted so you need an **Interpreter** (Later on, when we tell you how to install python, we truly tell you how to install the Python Interpreter). After the installation is done, you could fire up Notepad and write your code. Although ~~all~~ most of us would not recommend this.

 The next thing you would like to use is an Integrated Development Environment (IDE), the MatLab GUI is an example of an IDE. An IDE offers you syntax highlighting, code completion and it can point out errors in your code. Furthermore it normally comes with a green play button to run your program code. And it features a [debugger](#Debugging) (yes, there is a way more efficient way on squashing bug than using print statements). The most used IDEs at our institute are PyCharme and Spyder. Eclipse and Visual Studio are rarely used (and they are a bit more complicated to configure). You probably ask your advisor which IDE he uses and settle on the same.

- [ ] Abbildung Zusammenhang IDE / Sprache / Interpreter

An IDE can **not** run any code without an interpreter. Although PyCharme and Spyder are __Python only__ IDEs, Eclipse for example is not (and even Spyder and PyCharme will have to handle different language versions of Python). Depending on your installation, the IDE may be pre-configured to default to an Interpreter, but if your IDE is doing nothing, it is probably because it does not know how to do it. The good thing is: Every IDE has somewhere in its options something called "configure interpreter" (or something similar) and you just have to point it the python.exe in your python folder (see Installation Guide further down). The IDE will than do all the heavy lifting on its own.

- [ ] Add Link to a file that shows how to change the interpreter for the relevant IDEs


### Take away
Python is the description, how to write code, the interpreter translates your code to the PC, an IDE helps with code development. Python is **not** a piece of software, it is no Graphical User Interface (GUI) and, Peter Remmen asked to mention this: It is also not Teaser.
## What are packages and modules?
Python functions are ordered in a library, each element of the library is called a package and may contain several modules. Each of the modules may contain different methods or classes. If you would like to compare it to your file system on the computer, the package is a directory, each module a file and the methods and classes are the text in your files. Each Python distribution comes with a big library, but after startup, only a part of the library is loaded and available. If you need more parts of the library, you will have to import them, so most time your code will start with several import statements and look like this

``` python
import datetime as dt
import os.path
import pandas as pd
import pylab as plt
```

If you are writing code, you have to refer to a method with its package name before (or its alias, defined after the `as` statement), so if you would like to access the datetime object in the datetime library, you would have to write `dt.datetime` in your code. The advantage of this behavior is that this preserves the so called namespace. So you can have the variable `foo` in two packages, for example the packages `bar` and `baz`, because for python `bar.foo` is something completely different than `baz.foo`.

But how does Python "find" its library? Most packages came with your distribution and are stored in a place were python will find them. If you want to install additional packages, you should use pip to ensure that they are stored correctly [There is a user guide for it](https://pip.pypa.io/en/stable/user_guide/). Usage of pip is really easy but you have to make sure, you use the right version of pip, because there may be other python distributions on your system (we'll elaborate on how to use it later on).

### Take away
You'll have to use import statements because parts of Pythons library are not loaded on startup. If you need to install new software, use pip.

