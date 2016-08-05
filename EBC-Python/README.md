# Introduction

This is the EBCs Tutorial to use Python at our institute. This is **not** a tutorial to teach you the basics of programming or python. There are a lot better tutorials online (we included some links), we'd refer you to use those. 
So what will you find in this tutorial? You'll mainly find three things. At first we'll give a brief introduction into some aspects of programming. We want to make sure that we talk about the same things using the correct wording. If you are already familiar with those concepts: Great, if not, it may avoid some misunderstanding. The second one is an instruction how to get your python installation running. Following these instructions we'll make sure that
* all necessary packages are up to date
* you can access EBC libraries
* you don't use a version somebody may have toyed around with 

All of this will ensure that you can start working with Python without running into some nasty and unnecessary obstacles, keeping you away from getting work done.

In the third part we'll introduce some concepts that may help you to become better at programming, fit into EBCs style of programming (something we are still developing) and give you some ideas for a best practice that we expect to save you some time. We are not without faults, so if you find better or more efficient solutions: Feel free to suggest them. In the best case you contribute to our EBC Libraries via Git (it is a version control system. You can not destroy anything, so have no fear). The concepts are backed up by examples in an Jupyter Notebook. We don't expect everybody to understand all the examples, especially not at the beginning. But if you are planning your code and move forward in your project, we hope that some of these concepts resurface in your brain and you come back here to have a look. Everything in here has, for sure, already been written, probably in a better way. But here we have everything in one place, this is the true advantage of this tutorial.

In a nutshell we will

* make us use all the same wording
* get you started with the environment
* point you to some "learn to code" tutorials
* show you some concepts that may help you improving your coding efficiency (We made already a lot of mistakes for you, you do not have to re-do those)


# A short introduction 
## What is Python, and what not
Python is a programming language. Basically, a programming language is a set of instructions to tell the PC to do something. Every programming language has it's own grammar. And they are only theoretical constructs. You can not write software just with the language definition of python.
 
So obviously, you need some more stuff to get a programming language to do work. First of all, PCs don't understand text, they understand zeros and ones. So everything you have written, must be interpreted so you need an **Interpreter** (Later on, when we tell you how to install python, we truly tell you how to install the Python Interpreter). After the installation is done, you could fire up Notepad and write your code. Although ~~all~~ most of us would not recommend this.
 
 The next thing you would like to use is an Integrated Development Environment (IDE), the MatLab GUI is an example of an IDE. An IDE offers you syntax highlighting, code completion and it can point out errors in your code. Furthermore it normally comes with a green play button to run your program code. And it features a debugger (yes, there is a way more efficient way on squashing bug than using print statements). The most used IDEs at our institute are PyCharme and Spyder. Eclipse and Visual Studio are rarely used (and they are a bit more complicated to configure). You probably ask your advisor which IDE he uses and settle on the same.
 
- [ ] Abbildung Zusammenhang IDE / Sprache / Interpreter
 
An IDE can **not** run any code without an interpreter. Although PyCharme and Spyder are __Python only__ IDEs, Eclipse for example is not (and even Spyder and PyCharme will have to handle different language version of Python). Depending on your installation, the IDE may be pre-configured to default to an Interpreter, but if your IDE is doing nothing, it is probably because it does not know how to do it. The good thing is: Every IDE has somewhere in its options something called "configure interpreter" (or something similar) and you just have to point it the python.exe in your python folder (see Installation Guide further down). The IDE will than do all the heavy lifting on its own.
 
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


# How do I install Python?
We strongly recommend to follow these instructions step by step.

1. Create a folder on D:, name it something like 'my_name_my_python_installation' (and yes, you should **never** save something on 'D:/' because it is not backed up. Never except now...)

2. Download the current WinPython distribution from [WinPython Download Site](http://winpython.github.io/#releases). Click on Download and be a lemming, run with the herd: Download the must downloaded one. To avoid confusion: When we say 'Download it from...' we mean exactly this. We do not mean: Install it through the 'Softwareverteilung'. And to add some confusion: If you are expected to work with Gurobi (If you do not know, you are probably not expected to...), ask your advisor which version to download. I was told Gurobi and Python is sometimes a bit difficult

3. Save this in your folder created in step 1.
