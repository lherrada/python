def fetcher(obj,index):
 return obj[index]

if __name__ == '__main__':

 try:
  print fetcher('Luis',5) 
 except Exception as e:
  print "[%s] : %s" % (e.__class__.__name__,e) 
 finally:
  print "Continuing execution ..."

 print fetcher("Silvia",1)
