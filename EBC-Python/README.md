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
 
 The next thing you would like to use is an Integrated Developer Environment (IDE), the MatLab GUI is an example of an IDE. An IDE offers you syntax highlighting, code completion and it can point out errors in your code. Furthermore it normally comes with a green play button to run your program code. And it features a debugger (yes, there is a way more efficient way on squashing bug than using print statements). The most used IDEs at our institute are PyCharme and Spyder. Eclipse and Visual Studio are rarely used (and they are a bit more complicated to configure). You probably ask your advisor which IDE he uses and settle on the same.
 
 An IDE can **not** run any code without an interpreter. Although PyCharme and Spyder are __Python only__ IDEs, Eclipse for example is not (and even Spyder and PyCharme will have to handle different language version of Python). Depending on your installation, the IDE may be pre-configured to default to an Interpreter, but if your IDE is doing nothing, it is probably because it does not know how to do it.
 
### Take away
 Python is the description, how to write code, the interpreter translates your code to the PC, an IDE helps with code development. Python is **not** a piece of software, it is no Graphical User Interface (GUI) and, Peter Remmen asked to mention this: It is also not Teaser. 
