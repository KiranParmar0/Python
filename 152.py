def fun(no):
	if no%2 == 0:
		return 0 or True
	else:
		return 1 or False
def main():
	print("enter the no:")
	no =int(input())
	ret=fun(no)
	print(ret)
if __name__ == "__main__":
	main()