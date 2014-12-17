def addone(myfunc):
 def addoneinside():
  return myfunc() + 1
 return addoneinside

@addone
def oldfunc(): return 5 

#x=addone(oldfunc)
#print x()

'''
print oldfunc()
oldfunc=addone(oldfunc)
print oldfunc()
'''
print oldfunc()
