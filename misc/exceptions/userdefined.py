class Bad(Exception):
 pass

def doom():
 raise Bad

if __name__ == '__main__':
 try:
  doom()
 except Bad:
  print "Getting Bad exception"

 print "-"*30
 
 
