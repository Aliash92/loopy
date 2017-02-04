def pattern(p_statement):
	for i in range(0,(len(p_statement)+1)):
		print p_statement[:i]
		
sentence = raw_input("Enter a statement ")
pattern(sentence)
