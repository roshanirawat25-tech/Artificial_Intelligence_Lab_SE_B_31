
mech=float(input("enter marks of Mechanics:"))
M2=float(input("enter marks of Maths 2:"))
bxe=float(input("enter marks of Electronics:"))
phy=float(input("enter marks of Physics:"))
pps=float(input("enter marks of PPS:"))

Marks=(mech+M2+bxe+phy+pps)/5
print("Congratulations you got",Marks)

if Marks>75:
	print("diostinction")
	
elif 75>Marks>65:
	print("first class")
elif 65>Marks>40:
	print("second class")
else:
	print("fail")
