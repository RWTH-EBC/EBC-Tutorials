<a href="https://github.com/RWTH-EBC/EBC-Tutorials/README.md"><img src="PicsForChapters/0_Start_filled.png" height="40"></a><a href="1_Short_Introduction.md"><img src="PicsForChapters/1_A_Short_Introduction_filled.png" height="40"></a><a href="2_Install_Python.md"><img src="PicsForChapters/2_Install_Python_filled.png" height="40"></a><a href="3_Time_to_Say_Goodbye.md"><img src="PicsForChapters/3_Time_to_Say_Goodbye_filled.png" height="40"></a><a href="4_Advanced_Concepts.md"><img src="PicsForChapters/4_Advanced_Concepts_filled.png" height="40"></a>
<img src="PicsForChapters/tree.png" height="40" width="600" hspace="40"><p></p>
<p></p>
<a href="4-1_Jupyter_Notebook.md"><img src="PicsForChapters/4-1_Jupyter_Notebook_filled.png" height="40"></a> <a href="4-2_Plan_Your_Code.md"><img src="PicsForChapters/4-2_Plan_Your_Code_filled.png" height="40"></a> <a href="4-3_Creating_Plots.md"><img src="PicsForChapters/4-3_Creating_Plots_transparent.png" height="40"></a> <a href="4-4_Object_Orientation.md"><img src="PicsForChapters/4-4_Object_Orientation.png" height="40"></a> <a href="4-5_Debugging.md"><img src="PicsForChapters/4-5_Debugging.png" height="40"></a>

## Creating plots
Structuring plots can save a lot of time, and they represent the results of your work. You may want to get these plots right. We start with some general explanations, how matplotlib works and go on with some concepts that improve the reusability of your code.

A general [description](http://matplotlib.org/api/index.html) about available methods can be found on the [matplotlib homepage](http://matplotlib.org/api/index.html), they also have a [gallery](http://matplotlib.org/gallery.html) with source code to get some ideas how to create plots.

 To access our own examples stored in a Jupyter Notebook, please open the WinPython Command Prompt from your python distribution and then enter `jupyter notebook Git_path\EBC-Python-101\plotting.ipynb`. 'Git_path' is the path to your local working copy of the EBC_Tutorial repository. It may take several seconds, but the notebook should than open in your browser.
 
### Plotting: General remarks
We strongly recommend that you create plots at the size that you need them. If you include them into LaTeX, LaTeX does a great job in scaling them (especially if you use `\includegraphics[width=\textwidth{filename}`), but scaling will distort the size of your text and increase or decrease the size of your markers. If your original plots were of different size, there will be differences between the font size and the line size. You are better off to create two or three possible sizes and create every figure at one of those sizes. And if you need the same plots for a presentation: Do not scale them either. Re-plot them, with a more viewer friendly design and make sure that tools like PowerPoint may not like pdfs, so try to use different file formats for different applications (Using a good structured plot, it is really fast to re-create it)

The same comment is also valid for colors and markers: Use the same color and marker sequence to create similar looking plots.

Furthermore we would encourage you to create a metafile for each plot. This textfile should contain information which data you used to create the plot and which file and version to create the plot. 

There is a subpackage `ebcplots` in our Git-Repository. This package provides you with some convenience functions (some are already superseded by pylab functions), but the `optimize_and_save`-function is still very useful. This method also supports the writing of metadata about a file and contains design dictionaries for different usage scenarios (We get back to design dictionaries in the next section)

### Matplotlib: General introduction
You can import matplotlib with `import matplotlib`, but normally you would use `import pylab as plt`, which wraps some matplotlib functions conveniently. This is a bit confusing and sometimes you can not access methods via pylab, that exist in matplotlib. This is a rare event but keep in mind that you can access **all** matplotlib methods via `pylab.matplotlib.[...]`

Matplotlib uses a hierarchical system to create your plot, this means that a figure contains one or more pairs of axes, these axes contain the plotted data. Properties are normally located where you would look for them (axes labels at the axes, figure dimensions at the figure, linesize at the plot etc.) Therefore it is good practice to keep track of your figure and axes handles.

To store plotting defaults, matplotlib uses the (well hidden) rcParams and refers by default to the file `matplotlibrc` in its home folder (if you followed the instructions above, this should be `Path_to_your_installation\python-[version].amd[bit]\Lib\site-packages\matplotlib\mpl-data`). You can alter this file to ensure a general change in layout, but we would recommend to define several layout dictionaries and alter the rcParams for the current session with pylab.rcParams.update(design_dict). 

For an exemplary usage of different plot layouts have a look at the section *Configuring the plot layout* in the Jupyter Notebook *Plotting* in this repository.

#### Take away
Setup a dictionary for your layout, plot your figures directly in the size you need them and use just three different sizes for plotting if you want to use them in a document.

### Ensuring reusability
Keep your plotting functions simple, never plot more than **one** thing per plot! If you have datasets from two measurements, you could of course load them into Python and then plot them into one graph using a function that takes care of both datasets. The better method would be, to call the function twice with different parameters: Starting with the first dataset then the second. Because if you happen to get a third measurement, you could just call that function a third time. Even more: If one of the measurements is a reference value and you would like to create two plots: Each plot with the reference and one dataset, this can be easily achieved with that function. ![Create a figure from three subsequent function calls](https://michaeladolph.github.io/plotting_code_reusability.png).

To make a function work this way, your function needs at least two parameters: The data you want to plot and an axes handle, e.g. the place where you want your data to appear. With this method you can separate the creation of the figure and the layout of the figure. This is a flexibility you will surely appreciate.

See the section *Ensure the reusability of plots* section in the *Plotting* Notebook for examples.

#### Take away
A function plots only one dataset at once into the axes. Separate the layout of the figure from the content creation.

### Fine Tuning
This section covers the fine tuning of your plots. Everything in here is not necessary, but "nice to have" if you want to squeeze everything out of your work.

#### Make TeX render your Text
There is an option that lets matplotlib render your text by TeX, but it may cost you some effort. So why should you do it? It is just for the optics, the text in your figures will excactly resemble the text in your document. You can give it a shot if it works.

There is a general explanation on a [matplotlib site](http://matplotlib.org/users/usetex.html), but you can also  follow our short instruction. So, what do you need to make it work?

- Quite obvious a working LaTeX installation. If you use LaTeX, this should already be fine, and if you don't use LaTeX, you don't need your plots to look like LaTeX
- Ghostscript. This is not available through our software installation, but you can get a self-running version from ![portable apps](http://portableapps.com/apps/utilities/ghostscript_portable)
- Matplotlib must be able to know where to find Ghostscript, therefore add the Link to your path
    1. Click the windows start button
    2. Click the picture above your name in the right part of your window
    3. The control center will open with the user profiles opened ("Benutzerkonten" if you are using a system with German localization). Of course, you can get there with an alternative route
    4. In the window that just opend, there is the option to change your environmental variables ("Eigene Umgebungsvariablen ändern") on the left side - click it!
    5. There may already be a Variable on the top called PATH, if not: Create it by clicking new, otherwise chose it and push edit
    6. Name the variable "PATH" (if not already done so, the name is __not__ case sensitive), As value enter the complete path to the Ghostscript executable gswin64.exe 
    7. If not already in there, you must point matplotlib also to your mikTex Installation Folder, that should be located at a location similar to C:\Users\your_username\AppData\Roaming\MiKTeX\2.9\miktex\bin\x64\. The two paths are seperated by semicolon
    8. Never ask why Microsoft thought that would be a good layout or way to add environmental variables.
    9. Update your layout dictionaries to use tex.
        - ```your_design_dict['text.usetex'] = False```
        - ```your_design_dict['text.latex.unicode'] = True```
        - ```your_design_dict['text.latex.preamble'] = [r'\usepackage{fourier}', r'\usepackage{amsmath}', r'\usepackage[squaren]{SIunits}']```
        - If you used several dictionaries as suggested, update them as well

Now everything should theoretically work well. Because every text will be layouted using LaTeX, every text must be LaTeX compatible. And to avoide python to use so-called escape characters, you should declare every string as a raw-string by a preceeding 'r' and than follow normal LaTeX syntax. To create a Text saying Tset with the 'set' as subscript, you need to write
`r'T$_\text{set}$`. Note that we used the command `\text` to set the word 'set' upright, because it is normal text. And we used '$', because a subscript can only be set in formulas.

#####Take away
It is possible to let TeX Render your text, that looks awesome. But it can also cause trouble. Your decision to use it or not, an alternative would be [mathtext](http://matplotlib.org/users/mathtext.html#mathtext-tutorial).
