def sexy_pattern(pattern):
	print " " * 6,
	x = 6
	y = 12
	for i in range(1,6):
		print (pattern + " ") * i,
		print " " * y, (pattern + " ") * i
		x = x - 1
		y = y - 2
		print " " * x,
	x = 1
	y = 2
	for i in range(6,0,-1):
		print (pattern + " ") * i, " " * y, 
		print (pattern + " ") * i
		x = x + 1
		y = y + 2
		print " " * x,
			
		

exotic = raw_input("Please enter the desired pattern ")
sexy_pattern(exotic)