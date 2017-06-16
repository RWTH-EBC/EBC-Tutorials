#  Basic tutorial

You can find all example files of the basic tutorial in .../example_files folder.

##  Let's get startet: How to write a function in Python

Aim: Write a mathematical function, which (exclusively) squares integer numbers.
Thus, we are going to generate an Python file named example_1.py and write a function

	#  I am a function (defined by 'def')
	def square_int_number(number):
		squared_nb = number ** 2  # Square input number
		return squared_nb

functions are defined via keyword _"def"_. 
By default, functions hold brackets (optionally with input parameters), e.g.

	def name_of_function(input_1, input_2, input_3)

The Python interpreter (see Python.exe) is able to understand which parts of the code belong 
to the function by using _tabs_ to move the text. This combines good readability and code logic. 
The result is returned with the _"return"_ statement. 
Now, we are going to add a function call at the bottom.

	#  I am a function (defined by 'def')
	def square_int_number(number):
		squared_nb = number ** 2  # Square input number
		return squared_nb

	#  Execute function
	input_number = 2  # Input parameter
	#  Function call
	result_number = square_int_number(input_number)
	#  Print statement
	print('Squared number is:', result_number)

Code execution results in the print statement "Squared number is: 4".
The function call seems to deliver correct results. 
However, the function would accept floats, although we only wanted to process intergers.
To prevent squaring of floats, we are going to at an _assert_ statement.

	def square_int_number(number):
		#  Assert function. Checks if input parameter is of type integer
		assert isinstance(number, int), 'Input is not of type integer!'
		squared_nb = number ** 2  # Square input number
		return squared_nb

isinstance checks, if the input "number" is of type integer. If we have an integer as input,
isinstance returns True and the code processing is going to be continued. If we get a non-integer,
isinstance returns False, which will lead to the raise of an AssertionError. 
It can be elementary to stop code execution as early as possible, if wrong behavior occurs. 
Assert statements can help to do this. It might save you a lot of time in code debugging, later on.

Currently, we got a function call of 
	square_int_number()
on the highest indentation level (let's say, maximum left side ;-). 
This could cause us some trouble, if we would like to re-use the module example_1.py and its function(s)
in another module. We could use an 
	import 
statement to import the module example_1.py into our new module. However, during import, Python is going to
execute every Python statement, which is called. This results into automatically calling 
	#  Execute function
	input_number = 2  # Input parameter
	#  Function call
	result_number = square_int_number(input_number)
	#  Print statement
	print('Squared number is:', result_number)
during import. To exclude function execution we can add a 
	if __name__ == '__main__': 
to the bottom. If the module example_1.py is called, its name equals main. 
Thus, the if statement is True and all code lines within the if statement are executed. 
However, is example_1.py is imported from another module, example_1.py is not main, any more. 
Thus, the if statement is False.

	if __name__ == '__main__':
		#  Execute function
		input_number = 2  # Input parameter
		#  Function call
		result_number = square_int_number(input_number)
		#  Print statement
		print('Squared number is:', result_number)

Now, the function 
	square_int_number(input_number)
is only called if example_1.py is directly executed.

Here comes the full code:

	#  I am a function (defined by 'def')
	def square_int_number(number):
		#  Assert function. Checks if input parameter is of type integer
		assert isinstance(number, int), 'Input is not of type integer!'
		squared_nb = number ** 2  # Square input number
		return squared_nb

	if __name__ == '__main__':
		#  Execute function
		input_number = 2  # Input parameter
		#  Function call
		result_number = square_int_number(input_number)
		#  Print statement
		print('Squared number is:', result_number)

#  Docstrings - How to add documentation into your Python code

Now, we are going to add a _"docstring"_ to our function:

	def square_int_number(number):
		"""
		I am a docstring
		"""

The text within the the """ """ is readible, e.g. by documentation functions of IDEs Spyder and PyCharm.

Helpful entries are:
- Description of function (how does it work?)
- Input parameters (Name, type, description)
- Return parameter (Name, type, description)
- Annotations, References, Examples...

The Numpy docstring style is a good reference for usage:
[https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)

Now let us add an more elaborated docstring to our function:

	#  I am a function (defined by 'def')
	def square_int_number(number):
		"""
		Returns squared value of input number.

		Parameter
		---------
		number : int
			Integer input value

		Returns
		-------
		squared_nb : int
			Squared integer output value
		"""
		#  Assert function. Checks if input parameter is of type integer
		assert isinstance(number, int), 'Input is not of type integer!'
		squared_nb = number ** 2  # Square input number
		return squared_nb

