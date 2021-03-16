
y = int(input('     INGRESE UN NÚMERO: '));
def fibonacci(d):
	a=0
	b=1
	for k in range(d):
		c=a+b
		a=b
		b=c
	return b
for e in range(y):
	print(fibonacci(e))
