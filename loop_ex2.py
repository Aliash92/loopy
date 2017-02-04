def pattern2(p_new,x=0):
	for i in range(1,(int(x)+1)):
		print p_new * i

pattern_content = raw_input("Please enter the pattern to be printed ")
num_times = raw_input("Please enter the number of times to be printed ")

pattern2(pattern_content,num_times)		