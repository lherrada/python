#!/usr/bin/python

#List Comprenhensions

#The syntax is [ expr for var in list ]

def main():
 nums=[3,6,9,12] 

 squares=[n*n*n for n in nums]
 print squares

 sisters=('Silvia','Leslie','Melissa')
 
 conversion=[n.upper() for n in sisters]
 print conversion

if __name__ == '__main__':
 main()
