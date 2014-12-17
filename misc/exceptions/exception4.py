'''
spam='Hello Amazon'
print len(spam)
print spam[15]
print "----> LHM"
'''
def divnum(x,y):
 try:
  f=open('divlog.txt','a') 
  f.write("%d divide by %d equals %.3f\n" % (x,y,x/y))
 except Exception as e:
  f.write('%s: %.1f/%.1f\n' % (e,x,y))
  raise
 finally:
  print "Finally ..."
  f.close()
  
if __name__ == '__main__':
 divnum(30,4)
 divnum(101,21)
 divnum(45,0)


