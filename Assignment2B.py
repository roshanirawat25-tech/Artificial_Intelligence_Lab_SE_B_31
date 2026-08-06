print("Core SUBJECTS: Physics,Maths,Chemistry,Biology,Circuits,Programming")
sub=list((input("enter subjects you like and prefer first :").split(",")))
if "maths" and "physics" in sub:
	print("Suggested career path : Mechanical Engineering")
elif "programming" and "maths" in sub:
	print("Suggested Career path: Computer Engineering")
elif "biology" and "chemistry" in sub:
	print("Suggested Career path: Biotechnology")
elif "circuits" and "maths" in sub:
	print("Suggested Career path: Electronical Engineering")
