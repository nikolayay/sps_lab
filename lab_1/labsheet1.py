# coding: utf-8

# # Lab 1: Introduction to Python and Jupyter Notebooks with Python Kernel
#
# Python is an incredibly flexible programming language. It is an interpreted language, and is easy to write and debug. Moreover, hundreds of libraries are available to suit all your needs.
#
# In this lab we will introduce the Python programming language, as well as two important libraries we will use throughout the unit:
# - [NumPy](http://docs.scipy.org/doc/numpy/index.html), for scientific computation
# - [Matplotlib](http://matplotlib.org/contents.html), to plot any kind of data
#
#
# Both of the above libraries have a complete and very good documentation which can be used to learn other features of the libraries or for questions and examples. The documentation is available either online (links above) or via Python itself, e.g. `help(numpy.matrix)` in the Python interpreter.
#
#
# ### The Python programming language
#
# The basics of Python are available [here](https://learnxinyminutes.com/docs/python/).
#
# The three key concepts worth mentioning here are:
# - loose syntax: no need of semicolon to end a line (e.g. `;` in C)
# - importance of code **indentation**: `if`, `for`, and most statement blocks are identified by indentation (this replaces the curly braces `{` in other languages)
# - comments are introduced with `#`
#
# The classic way to launch Python programs is from the command line. Suppose we have the following `hello_world.py` file:
#
# ``` Python
# a = 2
# b = 2
# c = a + b
#
# message = 'Hello World! Did you know that {} + {} equals {}?'.format(a, b, c)
#
# print(message)
# ```
#
# `format` is a function of the `string` class. It works by substituting the placeholders `{}` contained in the string with the provided parameters, returning a new string. Notice how we do not have to specify the type of the variables we want to print, unlike the classic C-style `sprintf` methods available in many languages. The `format` function is very powerful and flexible, allowing complex output prints. You can find a nice  tutorial [here](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3).
#
# Now, if we type `python hello_world.py` in a shell (provided it is already installed, which is the case of most if not all Linux distributions), we should see the expected greeting message:
#
# ``` Bash
# $ python hello_world.py
# Hello World! Did you know that 2 + 2 equals 4?
# $
# ```
#
# Python can also run interactively (somewhat like MATLAB). Simply type `python` in a shell and try it out! Alternatively, a better interactive Python shell (with tab completion, plus other features) is provided by [IPython](http://ipython.org/). To use IPython, simply type `ipython` in your shell to launch an interactive python session.
#
#
# #### Python 3
#
# We strongly encourage you to use Python 3 as opposed to Python 2, which will reach its end of life by the end of 2019.
#
#
# ### Jupyter Notebook
#
# Python can be run on [Jupyter Notebook](http://jupyter.org/) too.
#
# Jupyter Notebook is a computing environment supporting various programing languages (Python, R, Lua, etc.) through the concept of kernels.
# It allows you to enrich your code with complex comments formatted in Markdown and $\LaTeX$, as well as to place the results of your computation right below your code. Beside, it has all the features provided by the ipython interpreter, like tab auto-completion.
#
# Jupyter Notebook runs as a web server. To run this lab sheet navigate to the folder containing the file `labsheet1.ipynb` and run Jupyter:
#
# ``` Bash
# cd Downloads
# jupyter notebook
# ```
# now open your favourite web browser and go to: [localhost:8888/notebooks](http://localhost:8888/notebooks). Select `labsheet1.ipynb` from the file tree by clicking it. To shut down the notebook simply close your browser window and in the terminal window running the backend press `<Ctrl-C>`, type `y`, and press `Return` key.
#
# Notebooks are organised in **cells**. A cell may contain either code (in our case, this will be Python code) or text, which can be easily and nicely formatted using the Markdown notation.
#
# To edit an already existing cell simply double-click on it. You can use the toolbar to insert new cells, edit and delete them.
#
# Cells can be run, by hitting `ctrl+enter` when editing a cell or by clicking on the `Run` button at the top. Running a Markdown cell will simply display the formatted text, while running a code cell will execute the commands executed in it.
#
# **Note**: when you run a code cell, all the created variables, implemented functions and imported libraries will be then available to every other code cell. However, it is commonly assumed that cells will be run sequentially in terms of prerequisites.
#
#
# #### Markdown language (and a bit of $\LaTeX$ and HTML)
# Markdown cells allow you to write fancy and simple comments: all of this is written in Markdown - double click on this cell to see the source. Introduction to Markdown syntax can be found [here](https://daringfireball.net/projects/markdown/syntax).
#
# As Markdown is translated to HTML upon displaying it also allows you to use pure HTML: more details are available [here](https://daringfireball.net/projects/markdown/syntax#html).
#
# Finally, you can also display simple $\LaTeX$ equations in Markdown thanks to `MathJax` support.
# For inline equations wrap your equation between `$` symbols; for display mode equations use `$$`.
#
#

# ## Importing the libraries
#
# Before we start this lab we need to import the aforementioned NumPy and Matplotlib libraries, which we can do with the following code:
#
# ``` Python
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# ```
# we use the `import` keyword and bind the libraries to the `np`, `plt` and `Axes3D` namespaces with the `as` keyword.
#
# Now instead of typing long commands like:
#
# ``` Python
# a = numpy.matrix('1 2; 3 4')
# ```
#
# we can do:
#
# ``` Python
# a = np.matrix('1 2; 3 4')
# ```
#
# The cell below also instructs the Python kernel to put all the plots below your code (`%matplotlib inline`) and sets some default parameters for the plots (`pylab`) to ensure better readability when using a jupyter notebook. This line isn't used for python scripts.
#
# **Note** that up until now all the cells encountered in this notebook are *markdown* cells. The cell below is the first *code* cell in our notebook.
#
# To import these packages into your workspace and set the plotting environment simply navigate to the cell bellow and **evaluate it** (see above for details).
#
# **Note** The number will increase and denotes the order of execution of each cell.

# In[10]:


import matplotlib.pylab as pylab
import numpy as np
from scipy import stats
from pprint import pprint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

get_ipython().run_line_magic('matplotlib', 'inline')
# notebook
pylab.rcParams['figure.figsize'] = (32.0, 24.0)
pylab.rcParams['font.size'] = 24


# #### Pretty printing
#
# If you find yourself in a situation where printing some variables gives you barely readable output, e.g.:
# ``` Python
# print([range(30), [4,5,6], range(17)])
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
# ```
# you can import the `pprint` - *Pretty Printing* function:
#
# ``` Python
# from pprint import pprint
# pprint([range(30), [4,5,6], range(17)])
# [[0,
#   1,
#   2,
#   3,
#   4,
#   5,
#   6,
#   7,
#   8,
#   9,
#   10,
#   11,
#   12,
#   13,
#   14,
#   15,
#   16,
#   17,
#   18,
#   19,
#   20,
#   21,
#   22,
#   23,
#   24,
#   25,
#   26,
#   27,
#   28,
#   29],
#  [4, 5, 6],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
# ```
# which can give you a better insight into your data.
#
# ### Python as simple calculator
#
# Let's do some programming now: open the Python (or IPython) interpreter by typing `python` (or `ipython`) in the command line and perform some simple calculations, e.g.:
#
# - `2 + 2`
# - `7 * 7`
# - `2 ** 10` (exponentiation)
# - `10 / 3`
# - `10 / 3.0`
#
# please consider the difference between the output of the last two commands. Are you running python 2 or 3?
#
#
# ## NumPy
#
# NumPy is designed for scientific computing. The similarities to MATLAB are described [here](https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html).
#
# NumPy defines its own arrays which can be created with either of the following:
#
# ``` Python
# np.matrix('1 2; 3 4; 5 6')
# np.matrix([[1, 2], [3, 4], [5, 6]])
# ```
#
# - The first method is MATLAB style where matrices are created from a string, where elements in rows are separated by whitespaces, and new rows are introduced by a semicolon.
# - The second method uses Python's lists and wraps around a normal python nested list.
#
# We strongly recommend using the latter approach.
# For more details, type `help(np.matrix)` in your Python console or visit online help [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html).
#
# As Python is an object oriented language, the difference between *function* and *object property* should be understood.
# An object instance, e.g. NumPy matrix `A = np.matrix('1 2; 3 4')` inherits all the functions from the class `numpy.matrix`. Therefore, to sum all elements of matrix `A` we can choose two approaches:
#
# - `A.sum()`, or
# - `np.matrix.sum(A)`.
#
# the first one is advisable.
#
# Moreover, some objects have *properties* (e.g. size or shape of a matrix). Instead of calling the size *function*, a matrix object has the size *property*, i.e.:
#
# - `A.shape`
# - `np.shape(A)`
#
# the first one is advisable.
#
# **Note: MATLAB and NumPy indices**
#
# Be careful with your indices!
# - in Python, indices start from `0`, like in any proper programming language
# - in MATLAB, they start from `1` (and rest assured, you'll hate this)
#
#
# ## Matplotlib
#
# Once your results are ready, a good way to interpret them is via *visualisation*: Matplotlib (in particular its `pyplot` module) is your friend here.
# For an overview of the kind of plots you can produce with it, have a look at [this](http://matplotlib.org/users/pyplot_tutorial.html) web page.
#
# **Note: there are two plotting approaches**:
#
# - via `plt` call
#
# ``` Python
# plt.scatter(x, y)
# plt.show()
# ```
# - via object creation
#
# ``` Python
# fig, ax = plt.subplots() # when called with no arguments will create only one plot
# ax.scatter(x, y)
# plt.show()
# ```
#
# both are equivalent, the second one is advisable when a finer control over the Matplolib's [axes class](https://matplotlib.org/api/axes_api.html) is needed.

# ## Let's start
#
# Let's play a little bit with NumPy and Matplotlib now.
#
# ### 1. Create a matrix
#
# Let's create two matrices, `A` and `B`:
#
# ``` Python
# A = np.matrix('2 3; 4 -1; 5 6')
# B = np.matrix([[5, 2], [8, 9], [2, 1]])
# ```
#
#
# Try now to do it yourself in the *code* cell below. Print the content and the shape of the two matrices after you've created them.
#
# **Note**: remember to __run__ the cell, as you'll need the variables `A` and `B` later!

# In[11]:


# write here your code


# ### 2. Matrix operations
#
# Once you've run the cell above, you should have matrices `A` and `B` loaded in memory.
#
# Perform now the following operations on these matrices:
#
# - $C = 3A$
# - $C = A + B$
# - $C = AB^T$
#
# For more details type `help(np.matrix.transpose)` in your Python console or visit online help [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.transpose.html).

# In[12]:


# write here the code to perform the above operations, and print your results


# ### 3. More matrix operations
#
# Calculate now the *mean*, *sum*, and *variance* of your matrices `A` and `B`, using `NumPy` functions/matrix properties `mean`, `sum`, `var`.
#
# Hint: `help(np.sum)` or look [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html).
# Hint: `help(np.mean)` or look [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html).
# Hint: `help(np.var)` or look [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.var.html#numpy.var).

# In[13]:


# write your code here


# ### 4. Loading data
#
# Load the file `data.dat` available on the lab's webpage into a matrix `D`.
# Check the dimensions of the loaded data.
#
# Tip: to load MATLAB files with NumPy pass the `delimiter=','` parameter to the appropriate `NumPy` method.
#
# Hint: `help(np.loadtxt)` or look [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html).
# Hint: `help(np.ndarray.shape)` or look [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html).

# In[14]:


# write your code here


# ### 5. Scatter plot
#
# Plot the first two columns of the matrix `D` as *2D* scatter plot, then plot the last three columns as a *3D* scatter plot.
#
# Study the axis properties of the figure, and learn how to:
#
# - label the axes
# - change the axes limits
# - add a grid to the plot
# - change the markers’ shape, size and colour
#
# Tip: For 3D plots use *3D projection*: `fig, ax = plt.subplots(subplot_kw={'projection' : '3d'})
# `.
# Tip: Marker style object documentation is available [here](http://matplotlib.org/1.4.0/api/markers_api.html).
#
# Hint: `help(plt.scatter)` or look [here](http://matplotlib.org/api/pyplot_api.html?highlight=scatter#matplotlib.pyplot.scatter).
# Hint: `help(plt.show)` or look [here](http://matplotlib.org/api/pyplot_api.html?highlight=show#matplotlib.pyplot.show).
# Hint: `help(plt.figure)` or look [here](http://matplotlib.org/api/pyplot_api.html?highlight=figure#matplotlib.pyplot.figure).
# Hint: `help(plt.subplots)` or look [here](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html).
# Hint: `help(plt.Axes.set_xlabel)` or look [here](http://matplotlib.org/api/axes_api.html?highlight=set_xlabel#matplotlib.axes.Axes.set_xlabel).
# etc.

# In[15]:


# write your code here


# ### 6. Histogram
#
# Compute and display the histogram of the values in the first column of your matrix.
#
# Tip: the histogram method returns some useful statistics.
#
# Hint: `help(plt.hist)` or look [here](http://matplotlib.org/api/pyplot_api.html?highlight=hist#matplotlib.pyplot.hist).

# In[16]:


# write your code here


# ### 7. Normal distribution
#
# Generate a random sequence of 1000 numbers from the normal distribution $\mathcal{N}(0,1)$ using the NumPy command `np.random.randn`.
# Compute then and display the histogram of the sequence based on 100 bins between -5 and 5 using the command `plt.hist`.
#
# Hint: `help(np.random.randn)` or look [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randn.html).
# Hint: `help(plt.hist)` or look [here](http://matplotlib.org/api/pyplot_api.html?highlight=hist#matplotlib.pyplot.hist).

# In[17]:


# write your code here


# ### 8. Saving your data to a file
#
# Save the generated sequence to a text file.
#
# Tip: to save your data in a format readable by both NumPy and MATLAB pass the `delimiter=','` parameter to the appropriate NumPy method.
#
# Hint: `help(np.savetxt)` or look [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html).

# In[18]:


# write your code here


# ### 9. Generating random data
#
# Generate a random sequence of 100 numbers from a uniform distribution using the NumPy function `np.random.rand`.
# Compute and display the histogram, and appreciate the difference between the two distributions.
#
# Hint: `help(np.random.rand)` or look [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.rand.html).
# Hint: `help(plt.hist)` or look [here](http://matplotlib.org/api/pyplot_api.html?highlight=hist#matplotlib.pyplot.hist).

# In[19]:


# write your code here


# ## The automarker
#
# Your coursework will be marked with an automarker (fully for CW1 and partially for CW2). The automarker works by running your Python program, passing in input the necessary arguments and retrieving the output, which must be printed to the standard output. The automarker will then compare the obtained result with the expected one, and will assign a mark to your program accordingly.
#
# Let's prepare now a very simple script to be submitted to SAFE in order to familiarise with the automarker submission. For this example, your code should simply take two numbers `a` and `b` and return their product. We have provided the following skeleton code:
#
# ``` Python
# from __future__ import print_function
#
# import sys
#
# def product(numbers):
#     """Function to return the product of two numbers
#     Params:
#         numbers: List of two numbers to be multiplied
#     Returns:
#         product of two numbers
#     """
#     #Write your solution here
#
#
# numbers = sys.argv[1:] # sys.argv contains the arguments passed to the program
# product(numbers)
# ```
#
# Let's stop a couple of minutes to talk about the new things we see in the above code:
#
#
# ##### `from __future__ import print_function`
#
# In Python 2 `print` can be either a *statement* or a *function*, whereas in Python 3 it is *only* a function. When used as a statement, the two syntaxes below are equivalent:
#
# ``` Python
# print 'printed using the statement' # print statement - this works only in Python 2
# print('printed using the function') # print function - works both in Python 2 and 3
# ```
#
# However, the `print` statement is available only in Python 2. To avoid potential syntax issues and ensure portability, we can force Python 2 to only use the `print` function like in Python 3. We do this with the line `from __future__ import print_function`.
#
# Notice that this kind of special import from the `future` must be put at the top of the script, before any other import. When we import the `print` function in Python 2 the `print` statement will no longer be usable. We highly recommend you to *never* use the `print` statement and *always* use its function counterpart!
#
# ##### `def product(numbers):`
#
# This defines a function called `product`, which takes in input one parameter, which is called `numbers`. Such parameter is a list containing the two numbers to be multiplied.
#
# ##### `sys.argv[1:]`
#
# `sys.argv` is a list containing the arguments passed to the program. Like in C++, Java and most languages, the first argument is the name of the file we are running. Our function `product` expects the input list to contain only two numbers. With the syntax `sys.argv[1:]` we are *slicing* the list `sys.argv`, i.e. we are getting only a portion of it. More precisely, we are getting all the elements starting from the second position (inclusive, remember Python is 0-indexed!) onwards, which amounts to simply removing the name of the script as needed. List slicing is a powerful feature in Python. You can read more about it [here](https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/).
#
#
# **Notice: Always make sure there is a newline character at the end of your printed output!** This is for the automarker to correctly retrieve your output. As long as you use the `print()` function (i.e. without setting the optional parameter `end` to a character different from `\n`) you'll be fine.
#
# ### Submitting your code
#
# Prepare a Python script that takes in input two arguments from the command line and returns their product.
#
# Name your file `lab_1_test.py` and submit it to SAFE.
