<a href="README.md"><img src="PicsForChapters/0_Start_filled.png" height="40"></a><a href="1_Short_Introduction.md"><img src="PicsForChapters/1_A_Short_Introduction_filled.png" height="40"></a><a href="2_Install_Python.md"><img src="PicsForChapters/2_Install_Python_filled.png" height="40"></a><a href="3_Time_to_Say_Goodbye.md"><img src="PicsForChapters/3_Time_to_Say_Goodbye_filled.png" height="40"></a><a href="4_Advanced_Concepts.md"><img src="PicsForChapters/4_Advanced_Concepts_filled.png" height="40"></a>
<img src="PicsForChapters/tree.png" height="40" width="600" hspace="40"><p></p>
<p></p>
<a href="4-1_Jupyter_Notebook.md"><img src="PicsForChapters/4-1_Jupyter_Notebook_filled.png" height="40"></a><a href="4-2_Plan_Your_Code.md"><img src="PicsForChapters/4-2_Plan_Your_Code_filled.png" height="40"></a><a href="4-3_Creating_Plots.md"><img src="PicsForChapters/4-3_Creating_Plots_filled.png" height="40"></a><a href="4-4_Object_Orientation.md"><img src="PicsForChapters/4-4_Object_Orientation_filled.png" height="40"></a><a href="4-5_Debugging.md"><img src="PicsForChapters/4-5_Debugging_transparent.png" height="40"></a>

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
```c```: continue debuggin until you hit (another) breakpoint 
```s```: step through the code (into the next function)
```n```: go to the next line of code
```l```: list source code for the current file (default: 11 lines including the being executed)


### Take away
There are more efficient ways to debug your program code the print statements, one is the use of the Python integreated debugger pdb.
