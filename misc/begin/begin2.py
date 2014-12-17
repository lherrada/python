#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
	#print 'Hello there', sys.argv[1]
	print 'Hello there'
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

def repeat(message,exclaim):
	"""Returns string several times
	"""
	result = message+message+message

	if exclaim:
	   print "Exclaim set"
	   result=result+'!!!'
	return result
	

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
