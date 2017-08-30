# python-addition-module-or-sum-module-blue-print
python addition or sum module blueprint


def addition(b):
	s=0
	for a in b:
		s+=float(a)
	print(s)
if __name__ == "__main__":
	while True:
		b=input("Enter value: seprtate by , :- ").split(',')
		addition(b)
		z=input("Do you want to continue(y/n) :")
		if z=='n':
			break
