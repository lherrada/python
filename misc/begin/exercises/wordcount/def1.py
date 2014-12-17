#!/usr/bin/python

myGlobal = 5

def main():
 func1()
 func2()

def func1():
    global myGlobal
    myGlobal = 42

def func2():
    print myGlobal


if __name__ == '__main__':
 main()
