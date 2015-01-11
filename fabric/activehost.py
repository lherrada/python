import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
from fabric.api import *

ah=open("active_hosts.txt",'w')

sites=["acch","cpsz","fjkl","fldg","flks","fohm","fonn","fopy","fxbk","fxha","fxjd","fxks","fxvy","gisz","gtly","gtwf","hpwl","hsnj","iacs","itji","itks","jahs","jawx","jbgp","lgnj","moks","nchm","pmdg","rowj","shqt","tpxm","uszj","wijk"]

env.skip_bad_hosts=True

def set_hosts():
 env.user="indigoadmin"
 for site in sites:
  for i in xrange(101,103):
   host="%sdcs%d.apple.com" % (site,i)
   env.hosts.append(host)

@parallel
def test_hosts():
 return run('true',warn_only=True) 

set_hosts()
with hide('output','running','warnings'), settings(warn_only=True,quiet=True):
 results=execute(test_hosts)
 for key in results:
  if not results[key]:
   ah.write(key+'\n')
 # print key,results[key]
