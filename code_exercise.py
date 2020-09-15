"""
#1  Print the number of integers in an array that are above the given input and the number that are below, e.g. for the array [1, 5, 2, 1, 10] with input 6, print “above: 1, below: 4”.

#2  Rotate the characters in a string by a given input and have the overflow appear at the beginning, e.g. “MyString” rotated by 2 is “ngMyStri”.

#3  If you could change 1 thing about your favorite framework/language/platform (pick one), what would it be?

Let us know if you have any questions! If you're good to go, please send us back your exercise at your convenience (please upload your response to a public git repository, such as Github).
"""

def prompt_user_for_int(prompt):
	# Prompts for the question's input and checks if an integer
	# accepts string prompt
	# returns integer input
	while True:
		num_in = input(prompt)
		try:
			num_in = int(num_in)
			break
		except ValueError:
			print('Invalid input. Please only input an integer.')
		except:
			print('An unexpected error occured of type ' + type(err) + '... exiting program.')
	return int(num_in)

def count_array_range(num_in, array): # Answer to exercise #1
	"""
	counts numbers in list above and below the input integer
	accepts input number and array
	prints result to specifications
	"""
	above, below = (0, 0)
	for num in array:
		if num < num_in: # if the input is greater than the number, increment above
			below += 1
		elif num > num_in: # if the input is less than the number, increment below
			above += 1
		else: # if the input and number are the same, ignore it
			pass
	print('above: %s, below: %s' % (above, below))

def rotate_string(num_in, my_string): # Answer to exercise #2
	""" 
	rotates a given string by the input amount
	accepts input number and string to rotate
	prints result to specifications
	"""
	num_rotate = num_in % len(my_string) # string repeats after rotating the length of the string, so get the remaining rotations after repeats
	first_part = my_string[-num_rotate:] # splits string starting from the right and going left input number of spaces
	second_part = my_string[:-num_rotate] # splits remaining characters
	result = first_part + second_part # adds overlap to beginning of string
	print(result)


if __name__ == '__main__':
	## Run through each exercise, prompting for input and printing responses ##
	array = [1,5,2,1,10]
	my_string = "MyString"

	# First exercise
	num_in = prompt_user_for_int('Please input an integer to compare to the array: ')
	count_array_range(num_in, array)
	
	# Second Exercise
	num_in = prompt_user_for_int('Please input an integer amount to rotate "MyString": ')
	rotate_string(num_in, my_string)