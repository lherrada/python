def main():
 try:
  print "Hello" + 1
 except Exception as e:
  #print dir(e)
  #print "-->",type(e.message)
  #print e.args
  print "Exception!!!"
  print e
  raise

 print "We continued ...."

if __name__ == '__main__':

 main() 

