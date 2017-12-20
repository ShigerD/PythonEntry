
numbers = [1,2,3,4,5,6,7,8,9]
even = []
odd = []
while len(numbers)>0:
	number = numbers.pop()
	if(number % 2 ==0) :
		print  'a even: ' ,number
