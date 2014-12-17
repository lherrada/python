#!/usr/bin/python

def main():
 print donuts(7)
 
 print both_ends('Guevara')
 print fix_start('aminoacidacisa')
 print mix_up('dog','dinner')

def donuts(count):
 if count < 10:
  return 'Number of donuts:' + str(count)
 else:
  return 'Number of donuts: many'

def both_ends(string):
 if len(string) < 2: return ' '
 else: return string[:2]+string[-2:]

def fix_start(string):
 return string[0]+string[1:].replace(string[0],'*')

def mix_up(stra,strb):
 return strb[0:2]+stra[2:] + ' ' + stra[0:2]+strb[2:] 


if __name__ == '__main__':
 main() 
 
