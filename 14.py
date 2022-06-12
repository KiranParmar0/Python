def area(radius,PI=3.14):
	return PI * radius*radius

def main():
	print("redius of the cricle") 
	cricl=area(int (input()))
	print("area of the cricle:",cricl)
	
	
if __name__ == "__main__":
	main()