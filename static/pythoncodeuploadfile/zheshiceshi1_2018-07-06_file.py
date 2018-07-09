
def f1(a,b,*c):
	n = 1
	m = 2
	n += m
	print(type(c))
	print(c[0],n)
	return a*b
def f2(a,b,**c):
	print(type(c))
	return c[1]*c[2]
