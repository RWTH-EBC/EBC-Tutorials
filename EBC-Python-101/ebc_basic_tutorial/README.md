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

In general: Try to break your code down in small, explicit functions instead of using long lines of code. 
It increases re-usability as well as code overview.	
		
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

#  pytests and unittests - How to test your Python code

You are probabily going to spend most of your programming time with debugging, less with coding the first version. 
Testing, especially automated testing, can save you a lot of debugging time. Different Python packages for testing exists, e.g.:
- unittest (Python in-built)
- pytest

Via unittest, pytest and co. you can test your functions and methods, if they perform the way to expect them to perform. 
This is mainly done by defining different inputs for each function and check the output with an assert statement. 
You can find an example pytest file under ../test_example_1.py

	class Test_Squaring(object):
		"""
		I am a test class for example_1.py based on pytest
		"""

		def test_positve_int(self):
			"""
			Testing method for positive integer inputs
			"""
			assert square_int_number(2) == 4

		def test_zero(self):
			"""
			Testing method for input zero
			"""
			assert square_int_number(0) == 0

		def test_negative_int(self):
			"""
			Testing method for negative integer inputs
			"""
			assert square_int_number(-2) == 4

You can call the test_example_1.py with execute_pytest_example.py.
Important: The names of the modules, which hold pytest cases, should start with test_ so that pytest is able to find the test cases.

You should get the following console output:
	collected 3 items

	test_example_1.py ...
	
Every dot represents one successful executed test case.

#  I am an object - Object-oriented programming in Python

__Objects__ can be suitable to model complex systems. Objects consist of __attributes__ and __methods__. 
We are going to define an own "Point" object:

	class Point(object):
		"""
		Point class
		"""

		#  Initialize Point object with x and y input parameters
		def __init__(self, x, y):
			"""
			Constructor of point object

			Parameter
			---------
			x : float
				x-coordinate in m
			y : float
				y-coordinate in m
			"""

			#  Hand over x and y as attributes to point object (self)
			self.x = x
			self.y = y

		def get_position_tuple(self):
			"""
			Returns position tuple of point object

			Returns
			-------
			pos : tuple (of floats)
				Position tuple, format (x, y)
				x : float
					 x-coordinate in m
				y : float
					y-coordinate in m
			"""
			pos = (self.x, self.y)
			return pos

Every object instance of class Point is initialized with 

	__init__()

x and y coordinates are necessary as input, e.g.

	i_am_a_point = Point(x=1, y=2)

__self__ is just the way to explicitly hand over the generated object instance to its own methods and access its own attributes, e.g. via:

	self.attribute  # Access attribute of object instance
	
Moreover, the Point class holds the method

	get_position_tuple()
	
to return the position tuple. 

Now, we are going to add some code to generate point objects and call the get_position_tuple() methods:

	if __name__ == '__main__':

		#  Generate two point objects
		point_1 = Point(0, 0)
		point_2 = Point(5, 10)

		#  Execute method get_position_tuple() of both point objects
		pos_1 = point_1.get_position_tuple()
		pos_2 = point_2.get_position_tuple()

		#  Print results (position tuples)
		print('Position tuple of point 1:', pos_1)
		print('Position tuple of point 2:', pos_2)

		#  Get x-coordinate of point 1
		x_coord = point_1.x
		print('x-coordinate of point 1 is:', x_coord)

Now, we are going to add another method to calculate the distance between two points

	def calc_distance_to_other_point(self, other_point):
		"""
		Calculates distance to other point.

		Parameters
		----------
		other_point : Point object
			Point object (of EBC Python Tutorial)

		Returns
		-------
		distance : float
			Distance between two point objects
		"""
		distance = ((self.y - other_point.y) ** 2 + 
					(self.x - other_point.x) ** 2) ** (1/2)
		return distance

To calculate the distance between two points, we are going to add:

	#  Calculate distance between point 1 and 2
	dist = point_1.calc_distance_to_other_point(point_2)
	print('Distance between point 1 and 2 is:', round(dist, 2))
