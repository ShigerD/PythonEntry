#!/usr/bin/python
class Employee:
	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount +=1

	def displayCount(self):
		print "Total Emplayee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name:", self.name,  ", Salary: ", self.salary 

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
print "Employee.__doc__:", Employee.__doc__
print "Employee.__doc__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
