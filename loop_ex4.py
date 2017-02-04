def multi_pattern(pattern):
	print " " * 6,
	x = 6
	for i in range(1,6):
		print (pattern + " ") * i 
		x = x - 1
		print " " * x,
	x = 1
	for i in range(6,0,-1):
		print (pattern + " ") * i
		x = x + 1
		print " " * x,
			
		

exotic = raw_input("Please enter the desired pattern ")
multi_pattern(exotic)