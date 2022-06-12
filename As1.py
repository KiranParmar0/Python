def Addition(LIST):
	sum = 0
	for i in range(0,len(LIST)):
		sum = sum + LIST[i]
	return sum

def main():
	print("Enter how many number print :")
	no= int(input())
	arr=list()
	
	for i in range(0,int(no)):
		num=input()
		arr.append(int(num))
	print("Entered Element are : ",arr)
	
	ret=Addition(arr)
	print("Addition is :",ret)

if __name__ =="__main__":
	main()
