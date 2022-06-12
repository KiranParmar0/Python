
def main():
	print ("enter the no to chek its even or odd:")
	no=int(input())
	if no%2== 0:
		print("no is even")
	else:
		print("no is odd")
	if no%3== 0:
		print("no is prim")
	else:
		print("no is notprim")
if __name__ == "__main__":
	main()