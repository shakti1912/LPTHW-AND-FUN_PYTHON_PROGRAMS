i = 0
numbers = []

def makeList(x):
	#i = 0
	numbers = []
	for i  in range(x):
		print "At the top i is %d" % i
		numbers.append(i)
	
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
makeList(10)
print "The numbers: "
for num in numbers:
	print num