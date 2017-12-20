#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import re

line = "www.runoob.com"
matchObj = re.match('www', 'www.runoob.com').span()
print  matchObj
print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runood.com'))



line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
print  matchObj
if matchObj:
	print "matchObj.group(0) : ", matchObj.group(0)
  	print "matchObj.group(1) : ", matchObj.group(1)
	print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"


line = "{\"code\":100000,\"text\":\"我20岁了，这是一个放纵自我的年纪。\"}"
pattern = '\"text\":\"(.*?)\"'
matchObj = re.search( pattern, line, re.M|re.I)
if matchObj:
	print "match --> matchObj.group() : ", matchObj.group()
	print "match --> matchObj.group() : ", matchObj.group(1)
	print "match --> matchObj.group() : ", matchObj.group(2)
else:
	print "text -No match!!"

#diff in match and search
line = "Cats are smarter than dogs";
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()

else:
	print "No match!!"

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print "search --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

