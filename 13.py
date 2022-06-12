import sys
def add( number,number1):
	return number + number1
	
def main():
	if len(sys.argv)<3 or (len(sys.argv)>3):
		print("Argument is Less than 3")
		return
	ret= add(int(sys.argv[1]),int(sys.argv[2]))
	print ("addition {} and {} is {}:".format(sys.argv[1],sys.argv[2],ret))
		
if __name__ == "__main__" :
	main()