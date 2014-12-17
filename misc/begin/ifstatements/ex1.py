#!/usr/bin/python
import sys

def main():
	print "This is my first if script"
	print repeat('Luis ',False,10)
	print repeat('Eliza ',True,4)

def repeat(message,exclaim,n):
  result=''

  for i in range(n):
   result =  result + message
   
  if exclaim:
	result=result+'!!!'	
 
  return result
   

if __name__ == '__main__':
	main()

sys.exit(1)


