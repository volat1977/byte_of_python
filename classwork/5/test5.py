employees = ['vasya Pupkin', 'Ivan Dulin']

d = {}
for employee in employees:
	names = employee.split(' ') # \n
	d[names[0]] = names[1]

print(d)
