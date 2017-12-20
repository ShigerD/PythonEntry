import urllib2
import urllib
def geturl(url):
	response = urllib2.urlopen(url)
	result = response.read()
	return result

def posturl(url, dataPost):	
	#dataPost = {'key':'21e76bf9a7f2418098dc514619c8bf00', 'info':'hello'}
	datalencode = urllib.urlencode(dataPost)
	request = urllib2.Request(url = url,data = datalencode)
	print request
	response = urllib2.urlopen(request)
	result = response.read()
	print result

#result = geturl('http://www.baidu.com/')
#print result

dataPost = {'key':'21e76bf9a7f2418098dc514619c8bf00', 'info':'hello', 'userid':'1'}

posturl('http://www.tuling123.com/openapi/api', dataPost)

	
