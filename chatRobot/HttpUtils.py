# -*- coding: utf-8 -*-
import urllib2
import urllib
class HttpUtils:
	def getUrl(self, url):
		response = urllib2.urlopen(url)
		result = response.read()
		return result

	def postUrl(self, url, dataPost):	
		#dataPost = {'key':'21e76bf9a7f2418098dc514619c8bf00', 'info':'hello'}
		datalencode = urllib.urlencode(dataPost)
		request = urllib2.Request(url = url,data = datalencode)
#		print request
		response = urllib2.urlopen(request)
		result = response.read()
#		print result
		return result

	def printSelf(self):
	        print(self)
	        print(self.__class__)
	
	def tuLinChat(self, info, id):
		httpUtil = HttpUtils()
		dataPost = {'key':'21e76bf9a7f2418098dc514619c8bf00', 'info':info, 'userid':id}
		tuLinRes = httpUtil.postUrl('http://www.tuling123.com/openapi/api',dataPost)
		return tuLinRes	
#result = getUrl('http://www.baidu.com/')
#print result

#dataPost = {'key':'21e76bf9a7f2418098dc514619c8bf00', 'info':'你好', 'userid':'1'}
#httpUtil = HttpUtils()
#httpUtil.getUrl('http://www.baidu.com')
#httpUtil.postUrl('http://www.tuling123.com/openapi/api',dataPost)
#httpUtil.printSelf()
	
