#!/usr/bin/python
import json

def main():

 f=open('json2.txt')
 data=json.load(f) 
 print data

 print json.dumps(data)

if __name__ == '__main__':
 main()
