
def Addsub (no,no1) :
	add = no + no1
	sub = no - no1
	mult= no * no1
	div= no / no1
	return add,sub,mult,div
	
def main():
	print ("Enter the 1st no:")
	a = int(input())
	print("Enter the 2nd no:")
	b = int(input())
	ret1,ret2,ret3,ret4= Addsub(a,b)
	print ("addition is:",ret1)
	print ("subtraction is:",ret2)
	print("Mlitipication is:",ret3)
	print ("div is:",ret4)

if __name__ == "__main__":
	main()