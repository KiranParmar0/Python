def Add(no,no1):
	values = no + no1
	return values
def main():
	print("enter the 1st no:")
	a = int (input ())
	print ("enter the 2nd no:")
	b=int(input())
	c=Add(a,b)
	print("The addition is :",c)


if __name__ == "__main__":
	main()