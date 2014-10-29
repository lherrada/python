import redis
import os
from os.path import join,getsize,isfile,isdir,islink
import re

def diskusage(dirpath):
 suma=0
 if isdir(dirpath):
  for root,dirs,files in os.walk(dirpath):
   try:
    suma+=sum([getsize(join(root,i)) for i in files if not islink(join(root,i))]
            + [getsize(join(root,i)) for i in dirs if isdir(join(root,i))])
   except Exception as e:
    pass
  return suma
 elif isfile(dirpath):
  return getsize(os.path.abspath(dirpath))
 else: return 0

def results(dirpath):
 assert isdir(dirpath),"Dirpath must be a directory"
 if not re.search(r'/$',dirpath):
  dirpath=dirpath+'/'

 rserver = redis.Redis('localhost')
 res=rserver.zrange(dirpath,0,-1,desc=True,withscores=True)

 if res:
  print "Data Found in redis"
  res=[(x,readable(y)) for (x,y) in res]
  return res 

 else:
  res=[]
  print "No data found. Recalculating ..." 

  #Recalculating subdirectories and files size
  for i in os.listdir(dirpath):
   mypath=dirpath+i
   res.append((mypath,diskusage(mypath)))

    #Store it in the cache
  pipe=rserver.pipeline()
  for x,y in res:
   #rserver.zadd(dirpath,x,y)
   pipe.zadd(dirpath,x,y)
  values=pipe.execute()
  #print values
   #Making expire in x seconds

  #Fetching the sorted results from Redis
  res=rserver.zrange(dirpath,0,-1,desc=True,withscores=True)
  rserver.expire(dirpath,30)

  #Converting from bytes to K,M or G bytes
  res=[(x,readable(y)) for (x,y) in res]
  return res

def readable(num):
 num=float(num)
 if num>1073741824:
  num=num/1024**3
  num=str("%.1f" % num) + 'G'
 elif num>1048576:
  num=num/1024**2
  num=str("%.1f" % num) + 'M'
 elif num>1024:
  num=num/1024
  num=str("%.1f" % num) + 'K'
 else: num=int(num)
 return num

if __name__ == '__main__':
 #mydir='/var/cache'
 #mydir='/home'
 mydir='/'
 print results(mydir)
