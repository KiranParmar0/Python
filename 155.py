def add(list):
	sum=0
	icnt=0
	while icnt< len(list):	
		sum = sum+list[icnt]
		icnt=icnt+1
	return sum

def main():
	arr = []
	print ("enter the no of elemnts :")
	size = int(input())
	for i in range(size):
		print ("enter the element no:",i+1)
		value =int(input())
		arr.append(value)
	print("accepet the data is:",arr)
	ret =add(arr)
	print("addition is :",ret)
	
if __name__ == "__main__":
	main()