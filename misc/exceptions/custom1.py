class CustomerError(Exception):
 pass

class C:
 pass

if __name__ == '__main__':
 raise CustomerError('My own exception')
 print CustomerError.__name__
 print CustomerError.__dict__
# print '-' * 30
# print dir(CustomerError.__bases__)

