def main():
 try:
  f=open('texto1.txt')
 except Exception as e:
  #print "CLASS: %s" % e.__class__.__name__
  print "%s[%s]: %s -> %s" % (e.__class__.__name__,e.errno,e.strerror,e.filename) 

if __name__=='__main__':
 print "---"
 main()
