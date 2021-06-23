
# Functional Programing (use f(), no 'for loop')
import random
#Generate 5 random numbers between 10 and 30
data = random.sample(range(10, 30), 5)
print(data)

def double(n):
	return n*2

res = map(double,data)
print(res)


