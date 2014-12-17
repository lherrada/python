from fabric.api import run,local

#def host_type():
#  run('uname -s')

def hello(name='Luis'):
 print("Hello World: %s" % name)

def message():
 print "MEsssage"

def overall():
 hello()
 message()
 local("df -h")

def host_type():
 run('uname -a')
