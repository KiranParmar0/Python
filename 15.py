def add(list):
	sum=0
	for icnt in range(len(list)):	
		sum = sum+list[icnt]
	return sum

def main():
	arr = [10,20,30,40,50]
	print (arr)
	ret =add(arr)
	print("addition is :",ret)
	
if __name__ == "__main__":
	main()