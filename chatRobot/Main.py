# -*- coding: utf-8 -*-
from HttpUtils import HttpUtils
import re


httpUtil = HttpUtils()
#baiduRes = httpUtil.getUrl("http://www.baidu.com")
#print baiduRes

tuLinUrl = 'http://www.tuling123.com/openapi/api'
mInfo = '你好'
mId = 3 
#	print("\033[0;37;46m%s\033[0m" % "输出青色背景")
#	print("\033[0;31m%s\033[0m" % "输出红色字符")

def regularStr(line):
	pattern = '\"text\":\"(.*?)\"'
	matchObj = re.search( pattern, line, re.M|re.I)
	if matchObj:
	#	print "match --> matchObj.group() : ", matchObj.group()
	#	print "match --> matchObj.group() : ", matchObj.group(1)
		return matchObj.group(1)
	else:
		print "text -No match!!"

while 1:
	mInfo = raw_input("\033[0;37;44m%s\033[0m" % 'Shiger: ')
	answer =  httpUtil.tuLinChat(mInfo, mId)
	answer = regularStr(answer)
	print("\033[0;37;46m%s\033[0m" % '小新: '+  "\033[0;36;47m%s\033[0m" % answer)
