#import utilities

print " ---> %s" % __name__
print " ---> %s" % __package__

if __name__ == "__main__" and __package__ is None:
    __package__ = "system1"
    print "-->" ,__package__

from . import utilities
utilities.message()

from .spam import spam_message

#print " ---> %s" % __package__
#print " ---> %s" % __name__

def average():
 print "This is the function average"
 spam_message()

