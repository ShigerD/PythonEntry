
def printFun(str):
	"print and string input"
	print str;
	return;

printFun("it is my frint");

a=[1,2,3];
print "a0" , a;
a="test str";
print "a1", a;


def printInfo(name, age):
	print "name:" ,name;
	print "age ", age;
	return;

printInfo(age=22,name="shiger");

def variableLengthFun(arg1, *vartuple):
	print "out:";
	print arg1;
	for var in vartuple:
		print var
	return ;
variableLengthFun(10,12,45,"string",a);


def printInfo(name, age):
	return name + age;
str =printInfo('shige','20'); 
print str ;

total = 0;
def sum(arg1, arg2):
	total = arg1 + arg2;
	print "total in sum :" , total;
	return;
sum( 10, 20);
print "total outside", total;
def sum2(arg1, arg2):
	global total 
	total = arg1 + arg2;
	print "total in sum2 :" , total;
	return;
sum2( 10, 20);
print "total outside", total;

