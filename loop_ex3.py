def pattern_exotic(pattern):
	print " " * 6,
	x = 6
	for i in range(1,6):
		print (pattern + " ") * i 
		x = x - 1
		print " " * x,
	
			
		

exotic = raw_input("Please enter the desired pattern ")
pattern_exotic(exotic)

