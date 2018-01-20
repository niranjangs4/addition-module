# Developed By : NIRANJAN KUMAR G S 
# From : INDIA
# Email : niranjan4@outlook.in
# Updated date : 12/Dec/2017


def addition(b):
	s=0
	for a in b:
		s+=float(a)
	print(s)
if __name__ == "__main__":
	while True:
		b=raw_input("Enter value: seprtate by , :- ").split(',')#python2
		#b=input("Enter value: seprtate by , :- ").split(',')	#python3
		addition(b)
		z=raw_input("Do you want to continue(y/n) :") 		#python2
		z=input("Do you want to continue(y/n) :") 		#python3
		if z=='n':
			break
