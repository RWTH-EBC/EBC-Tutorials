# Table of Contents

1. [Introduction](#introduction)
1. [A short introduction](#a-short-introduction)
    1. [What is Python, and what is it not](#what-is-python-and-what-is-it-not)
    1. [What are packages and modules?](#what-are-packages-and-modules)
1. [How do I install Python?](#how-do-i-install-python)
1. [Time to say goodbye](#time-to-say-goodbye)
1. [Advanced concepts](#advanced-concepts)
    1. [What is a Jupyter Notebook](#what-is-a-jupyter-notebook)
    1. [Plan before you code](#plan-before-you-code)
    1. [Creating plots](#creating-plots)
        1. [Plotting: General remarks](#plotting-general-remarks)
        1. [Matplotlib: General introduction](#matplotlib-general-introduction)
        1. [Ensuring reusability](#ensuring-reusability)
        1. [Fine Tuning](#fine-tuning)
            1. [Make TeX render your Text](#make-tex-render-your-text)
    1. [Object Orientation](#object-orientation)
    1. [Debugging](#debugging)

﻿﻿**This is currently under construction**

# Introduction
[Go back :arrow_up:](#table-of-contents)


This is a Tutorial to use Python at our institute. This is **not** a tutorial to teach you the basics of programming or python. There are a lot better tutorials online (we included some links), we'd refer you to use those.
So what will you find in this tutorial? You'll mainly find three things. At first we'll give a brief introduction into some aspects of programming. We want to make sure that we talk about the same things using the correct wording. If you are already familiar with these concepts: Great, if not, it may avoid some misunderstandings. The second one is an instruction how to get your python installation running. With following these instructions you'll make sure that
* all necessary packages are up to date
* you can access EBC libraries
* you don't use a version somebody may have toyed around with

This will ensure that you can start working with Python without running into some nasty and unnecessary obstacles, keeping you away from getting work done.

In the third part we'll introduce some concepts that may help you to become better at programming, fit into EBC's style of programming (something we are still developing) and give you some ideas for a best practice that we expect to save you some time. We are not without faults, so if you find better or more efficient solutions: Feel free to suggest them. In the best case you contribute to our EBC Libraries via Git (it is a version control system. You can not destroy anything, so have no fear). The concepts are backed up by examples in Jupyter Notebooks. We don't expect everybody to understand all the examples, especially not at the beginning. But if you are planning your code and move forward in your project, we hope that some of these concepts resurface in your brain and you come back here to have a look. Everything in here has, for sure, already been written, probably in a better way. But here we have everything in one place, this is the true advantage of this tutorial.

In a nutshell we will

* make us use all the same wording
* get you started with the environment
* point you to some "learn to code" tutorials
* show you some concepts that may help you improving your coding efficiency (We made already a lot of mistakes for you, you do not have to re-do those)

In the end, we want you to be able to use EBC's own Python libraries and even advance them. You should also recognize the advantages of object orientation and be able to use it.

# A short introduction
[Go back :arrow_up:](#table-of-contents)
## What is Python, and what is it not
Python is a programming language. Basically, a programming language is a set of instructions to tell the PC to do something. Every programming language has it's own grammar. And they are only theoretical constructs. You can not write software just with the language definition of python.

So obviously, you need some more stuff to get a programming language to do work. First of all, PCs don't understand text, they understand zeros and ones. So everything you have written, must be interpreted so you need an **Interpreter** (Later on, when we tell you how to install python, we truly tell you how to install the Python Interpreter). After the installation is done, you could fire up Notepad and write your code. Although ~~all~~ most of us would not recommend this.

 The next thing you would like to use is an Integrated Development Environment (IDE), the MatLab GUI is an example of an IDE. An IDE offers you syntax highlighting, code completion and it can point out errors in your code. Furthermore it normally comes with a green play button to run your program code. And it features a [debugger](#Debugging) (yes, there is a way more efficient way on squashing bug than using print statements). The most used IDEs at our institute are PyCharme and Spyder. Eclipse and Visual Studio are rarely used (and they are a bit more complicated to configure). You probably ask your advisor which IDE he or she uses and settle on the same.

- [ ] Abbildung Zusammenhang IDE / Sprache / Interpreter

An IDE can **not** run any code without an interpreter. Although PyCharme and Spyder are __Python only__ IDEs, Eclipse for example is not (and even Spyder and PyCharme will have to handle different language versions of Python). Depending on your installation, the IDE may be pre-configured to default to an Interpreter, but if your IDE is doing nothing, it is probably because it does not know how to do it. The good thing is: Every IDE has somewhere in its options something called "configure interpreter" (or something similar) and you just have to point it the python.exe in your python folder (see Installation Guide further down). The IDE will than do all the heavy lifting on its own.

- [ ] Add Link to a file that shows how to change the interpreter for the relevant IDEs

[Go back :arrow_up:](#table-of-contents)
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

[Go back :arrow_up:](#table-of-contents)
### Take away
You'll have to use import statements because parts of Pythons library are not loaded on startup. If you need to install new software, use pip.


# How do I install Python?


We strongly recommend to follow these instructions step by step.

1. Create a folder on D:, name it something like 'my_name_my_python_installation' (and yes, you should **never** save something on 'D:/' because it is not backed up. Never except now...).

2. Download the current WinPython distribution from [WinPython Download Site](http://winpython.github.io/#releases). Click on Download and be a lemming, run with the herd: Download the most downloaded one. To avoid confusion: When we say 'Download it from...' we mean exactly this. We do not mean: Install it through the 'Softwarecenter'. And to add some confusion: If you are expected to work with Gurobi (If you do not know, you are probably not expected to...), ask your advisor which version to download. Gurobi and Python can sometimes be a bit difficult.

3. Save this in your folder created in step 1.

- [ ] Welche EBC eigenen Libraries sollen eingebunden werden, Vorschläge bitte hinzufügen
- EBC Python Library
- AixPy
- [ ] Methodik, wie diese (sich in Entwicklung befindlichen) Pakete installieren lassen
- [ ] Link zu einer Erklärung, was die unterschiedlichen Pip Installationsvarianten tun (-e, wheel...)
- [ ] Hier muss dann auch noch der Hinweis hin, dass sie immer ihre Kommandozeile verwenden sollen.
- [ ] Das Cycler Paket muss installiert werden (benötigt fürs plotten, sonst folgend ständig deprecated Warnungen)

[Go back :arrow_up:](#table-of-contents)
# Time to say goodbye

This is the part, where we would like to wish you good bye for some time. Go away and learn Python (but ignore any tutorials how to install python. We got you covered above). If you aren't an experienced programmer, learning python will take some time. But doing it now correctly will save you a lot of time later on. And based on experience: Most students have enough time at the start of their thesis, at the end it is sometimes a bit more exhausting... .

- For those of you who read, [A Byte of Python](http://python.swaroopch.com/) is not only a silly pun but also a good introduction to Python. May take you some days to work through it.
- A [youtube playlist](https://www.youtube.com/playlist?list=PLkHsKoi6eZnwpn7P5G8gEBebAY8Jbky4N) with a fundamental programming course in Python from coursera (its about twice as long as Batman v. Superman but at least twice as fun!)
- If you are really ambitious, you may want to take the really good (but also really time consuming) Python course on [edx](https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-8).
- We'd also suggest that you take a short look at pandas, this is a package that can really help you to get work done. There is a [10 minutes to pandas](http://pandas.pydata.org/pandas-docs/stable/10min.htmlhttp://pandas.pydata.org/pandas-docs/stable/10min.html) guide, we are sure this won't be the 10 most wasted minutes in your life (remember the "cute cat" videos you watched last week? Or the last lecture you attended?).
- For specific questions on programming, [stackoverflow](http://stackoverflow.com/) is normally the place to go.

How deep you dive into learning to code is probably up to your interest and specific needs. We think that the ability to code efficiently is a key requirement (but we are also the guys that fancy [octocat](https://octodex.github.com/), so your mileage may vary). But before you continue, you should have at least an idea about these concepts (and if all of the concepts below are already clear to you: You may directly proceed):

- [ ] What are objects, and what is inheritance?
- [ ] What is the difference between a class and an instance?
- [ ] Your class `bar` has the attribute `foo`, how do you change it?
- [ ] What is a list comprehension?
- [ ] Why is this a bad way of using a for loop (hint: Iterate over the list itself)?:
```python
numbers = [1,2,3]
for i in xrange(3):
    print(numbers[i] * numbers[i])
```
[Go back :arrow_up:](#table-of-contents)
# Advanced concepts


We don't know if the concepts we suggest are really that advanced, but we believe that they may be helpful. Besides introducing those concepts, we tried to back them up with some examples, presented in Jupyter notebooks

[Go back :arrow_up:](#table-of-contents)
## What is a Jupyter Notebook
A Jupyter Notebook is a Textfile, similar to this one, but besides layouted text, it allows you to include program code that can be executed. You can start a Jupyter Notebook by entering `jupyter notebook <path_to_the_notebook>` into the WinPython Command Prompt of your Python installation. It will take some time and then open it in your browser. The Jupyter Notebooks reside in the same folder of the git Repository as this file. Before you start it, make sure you got the latest version by pulling from the repository.

[Go back :arrow_up:](#table-of-contents)
## Plan before you code
Yes, you probably have heard that before, and yes, each of us also started coding before thinking. Most time it is a bad decision, because it costs you time, you run into errors you would have avoided otherwise and maintaining the code is difficult.

So before you code, you should have a goal, for example: I want to plot the measured temperature data of two measurements. So, what are your steps:

- Reading the data from the measurement file into python
- handle the data (even if temperatures where measured, you may want to check for measurement errors, missing data etc.)
- create the plot and save it

So you have at least three functions: Read the data, clean the data, create the plot. And if cleaning the data is some more work, this may be more than one function. After you got an idea, which functions you need, write the documentation for the functions. This will force you to do three things:

- Describe in one sentence, what the function does. If it this is difficult and/or contains a lot of "and"s, your function is probably too complex and should be broken down into some more functions
- Think about the input: What type of data is coming into your functions, may several data types be possible? Are there optional parameters to change the behavior of the function?
- Think about the output: What type of data does your data return? Is this always the same data type (it should be, because subsequent functions may expect a special data type)

If some of your functions are very similar, you may consider to write a smaller function, that is called by the other functions (if there is a bug in your code, you have to fix it only in one place, not in 42). And after you wrote the documentation (please write it as docstring and adhere to the [docstring standards](https://www.python.org/dev/peps/pep-0257)), write the pseudo-code. That is a verbal expression of what you expect the code to do. This helps you to structure your work further, anticipate problems and works as documentation afterwards.

Yes, this all sounds boring. But it may save you some time. Time you could use to get your adrenaline kick elsewhere. And honestly: Otherwise you will be debugging the code more often. That is way more boring than creating code.

[Go back :arrow_up:](#table-of-contents)
### Take away
Think what you want to achieve, structure this into functions, make up your mind about parameters and return values. Write the documentation. Write pseudo code. Now you may proceed to start coding.

## Creating plots
Structuring plots can save a lot of time, and they represent the results of your work. You may want to get these plots right. We start with some general explanations, how matplotlib works and go on with some concepts that improve the reusability of your code.

A general [description](http://matplotlib.org/api/index.html) about available methods can be found on the [matplotlib homepage](http://matplotlib.org/api/index.html), they also have a [gallery](http://matplotlib.org/gallery.html) with source code to get some ideas how to create plots.

 To access our own examples stored in a Jupyter Notebook, please open the WinPython Command Prompt from your python distribution and then enter `jupyter notebook Git_path\EBC-Python-101\plotting.ipynb`. 'Git_path' is the path to your local working copy of the EBC_Tutorial repository. It may take several seconds, but the notebook should then open in your browser.
 
[Go back :arrow_up:](#table-of-contents)
### Plotting: General remarks
We strongly recommend that you create plots at the size that you need them. If you include them into LaTeX, LaTeX does a great job in scaling them (especially if you use `\includegraphics[width=\textwidth{filename}`), but scaling will distort the size of your text and increase or decrease the size of your markers. If your original plots were of different size, there will be differences between the font size and the line size. You are better off to create two or three possible sizes and create every figure at one of those sizes. And if you need the same plots for a presentation: Do not scale them either. Re-plot them, with a more viewer friendly design and make sure that tools like PowerPoint may not like pdfs, so try to use different file formats for different applications (Using a good structured plot, it is really fast to re-create it)

The same comment is also valid for colors and markers: Use the same color and marker sequence to create similar looking plots.

Furthermore, we would encourage you to create a metafile for each plot. This textfile should contain information which data you used to create the plot and which file and version to create the plot. 

There is a subpackage `ebcplots` in our Git-Repository [EBC_Python_Library](https://git.rwth-aachen.de/EBC/EBC_Python_Library). This package provides you with some convenience functions (some are already superseded by pylab functions), but the `optimize_and_save`-function is still very useful. This method also supports the writing of metadata about a file and contains design dictionaries for different usage scenarios. (We get back to design dictionaries in the next section.)
[Go back :arrow_up:](#table-of-contents)
### Matplotlib: General introduction
You can import matplotlib with `import matplotlib`, but normally you would use `import pylab as plt`, which wraps some matplotlib functions conveniently. This is a bit confusing and sometimes you can not access methods via pylab, that exist in matplotlib. This is a rare event but keep in mind that you can access **all** matplotlib methods via `pylab.matplotlib.[...]`

Matplotlib uses a hierarchical system to create your plot, this means that a figure contains one or more pairs of axes, these axes contain the plotted data. Properties are normally located where you would look for them (axes labels at the axes, figure dimensions at the figure, linesize at the plot etc.) Therefore it is good practice to keep track of your figure and axes handles.

To store plotting defaults, matplotlib uses the (well hidden) rcParams and refers by default to the file `matplotlibrc` in its home folder (if you followed the instructions above, this should be `Path_to_your_installation\python-[version].amd[bit]\Lib\site-packages\matplotlib\mpl-data`). You can alter this file to ensure a general change in layout, but we would recommend to define several layout dictionaries and alter the rcParams for the current session with pylab.rcParams.update(design_dict). 

For an exemplary usage of different plot layouts have a look at the section *Configuring the plot layout* in the Jupyter Notebook *Plotting* in this repository.

[Go back :arrow_up:](#table-of-contents)
#### Take away
Setup a dictionary for your layout, plot your figures directly in the size you need them and use just three different sizes for plotting if you want to use them in a document.

### Ensuring reusability
Keep your plotting functions simple, never plot more than **one** thing per plot! If you have datasets from two measurements, you could of course load them into Python and then plot them into one graph using a function that takes care of both datasets. The better method would be, to call the function twice with different parameters: Starting with the first dataset then the second. Because if you happen to get a third measurement, you could just call that function a third time. Even more: If one of the measurements is a reference value and you would like to create two plots: Each plot with the reference and one dataset, this can be easily achieved with that function. ![Create a figure from three subsequent function calls](https://github.com/RWTH-EBC/EBC-Tutorials/blob/master/EBC-Python-101/img/plotting_code_reusability.pdf)

To make a function work this way, your function needs at least two parameters: The data you want to plot and an axes handle, e.g. the place where you want your data to appear. With this method you can separate the creation of the figure and the layout of the figure. This is a flexibility you will surely appreciate.

See the section *Ensure the reusability of plots* section in the *Plotting* Notebook for examples.

[Go back :arrow_up:](#table-of-contents)
#### Take away
A function plots only one dataset at once into the axes. Separate the layout of the figure from the content creation.

### Fine Tuning
This section covers the fine tuning of your plots. Everything in here is not necessary, but "nice to have" if you want to squeeze everything out of your work.
[Go back :arrow_up:](#table-of-contents)
#### Make TeX render your Text
There is an option that lets matplotlib render your text by TeX, but it may cost you some effort. So why should you do it? It is just for the optics, the text in your figures will excactly resemble the text in your document. You can give it a shot if it works.

There is a general explanation on a [matplotlib site](http://matplotlib.org/users/usetex.html), but you can also  follow our short instruction. So, what do you need to make it work?

- Quite obvious a working LaTeX installation. If you use LaTeX, this should already be fine, and if you don't use LaTeX, you don't need your plots to look like LaTeX
- Ghostscript. This is not available through our software installation, but you can get a self-running version from [portable apps](http://portableapps.com/apps/utilities/ghostscript_portable)
- Matplotlib must be able to know where to find Ghostscript, therefore add the Link to your path
    1. Click the windows start button
    2. Click the picture above your name in the right part of your window
    3. The control center will open with the user profiles opened ("Benutzerkonten" if you are using a system with German localization). Of course, you can get there with an alternative route
    4. In the window that just opend, there is the option to change your environmental variables ("Eigene Umgebungsvariablen ändern") on the left side - click it!
    5. There may already be a Variable on the top called PATH, if not: Create it by clicking new, otherwise chose it and push edit
    6. Name the variable "PATH" (if not already done so, the name is __not__ case sensitive). As value enter the complete path to the Ghostscript executable gswin64.exe 
    7. If not already in there, you must point matplotlib also to your mikTex Installation Folder, that should be located at a location similar to C:\Users\your_username\AppData\Roaming\MiKTeX\2.9\miktex\bin\x64\. The two paths are seperated by semicolon
    8. Never ask why Microsoft thought that would be a good layout or way to add environmental variables.
    9. Update your layout dictionaries to use tex.
        - ```your_design_dict['text.usetex'] = False```
        - ```your_design_dict['text.latex.unicode'] = True```
        - ```your_design_dict['text.latex.preamble'] = [r'\usepackage{fourier}', r'\usepackage{amsmath}', r'\usepackage[squaren]{SIunits}']```
        - If you used several dictionaries as suggested, update them as well

Now everything should theoretically work well. Because every text will be layouted using LaTeX, every text must be LaTeX compatible. And to avoide python to use so-called escape characters, you should declare every string as a raw-string by a preceding 'r' and then follow normal LaTeX syntax. To create a Text saying Tset with the 'set' as subscript, you need to write
`r'$T_\text{set}$'`. Note that we used the command `\text` to set the word 'set' upright, because it is normal text. And we used '$', because a subscript can only be set in formulas.

[Go back :arrow_up:](#table-of-contents)
#### Take away
It is possible to let TeX Render your text, that looks awesome. But it can also cause trouble. Your decision to use it or not, an alternative would be [mathtext](http://matplotlib.org/users/mathtext.html#mathtext-tutorial).

## Object Orientation
Object orientation is not the simplest possible programming method and it may take some time to be able to completely understand and endorse it. But if you have a slight idea about object orientation, it can save you some time. And for those of you who use Modelica: That one is also object oriented, so maybe one could expect some synergies.

The thing I like most about objects is, that they wrap information neatly together, you may add some additional information, you can define methods that help you handle your data, and from the outside: All instances look the same and behave the same.

Whatever you do in your work, you'll often have things that are basically the same, but with different data. That may be 10 different runs of an experiment, each with some changes in the hardware, or 1000 simulations with different parameters. You will try to compare them and figure out, which effects the changes have. So one base object would be at least an object to keep your experiment data and another object to keep those objects for comparison.

The difference between a class and the instance of a class is often described as the difference between a recipe and the cake. The recipe is the theoretically description how to bake cake, and the cake is - the cake. And often you can re-use parts of a recipe (throw everything in a bowle, mix it, put it in the oven), change some things (ingredients, time in the oven) and create a completely new cake. The realization of a recipe is the cake, same is true for a class, the realization is the instance. And as you can create several cakes from one recipe, you can also create several instances from one class.

The Jupyter Notebook ObjectOrientation in this folder gives some more ideas why object orientation can be helpful.

[Go back :arrow_up:](#table-of-contents)
### Take away
Using object orientation simplifies your work by keeping your data structured. 

## Debugging
Like mentioned above, there is a more efficient way to debug your programs then using print statements. Therefore, Python has a build-in debugger, which is ready to use and waits for your use. Some IDEs come with a GUI support for the Python Debugger called pdb. However, we'll now start from the Stone Age and learn how to use the debugger without the green, blue, red or whatever colour it is debugger play button. So what does the Python Debugger do and how can we use this? Basically the Debugger stops your Python program at a certain point, the so called breakepoint, interactively. That means that your program is stopping there, but you can still interact with it. Interact in this case means, that you can define new variables, show existing variables, inspect and analyse objects and so on.

How to use:
``` python
import pdb #this imports the debugger module

pdb.set_trace() #this sets the actual breakpoint
```
Because you don't want to import the debugger in every file at top, we recommend using the pdb and breakpoint setting in a oneliner:
``` python
import pdb; pdb.set_trace() # import and breakpoint setting
```
Simple use this oneliner at a point in your code where you expect things going wrong. After this import the Python Interpreter jumps into the interactive Python Debugger. To demonstrate the use and capability of the debugger in comparison to print statements.... nahh you can do this on your own, so just a quick demonstration on how to use it.

Include gif of python debugger here

Handy commands:
`c`: continue debugging until you hit (another) breakpoint 
`s`: step through the code (into the next function)
`n`: go to the next line of code
`l`: list source code for the current file (default: 11 lines including the being executed)

### Take away
There are more efficient ways to debug your program code then print statements, one is the use of the Python integreated debugger pdb.

[Go back :arrow_up:](#table-of-contents)
