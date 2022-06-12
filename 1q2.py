def chkNum(no):
	if no%2 ==0:
		return True
	else:
		return False
def main():
	print ("Enter the No to chek given No is even or Odd:")
	a = int(input())
	c= chkNum(a)
	if c==True:
		print(" {} this No is Even No".format(a))
	else:
		print ("{} this No is Odd NO".format(a))

if __name__ == "__main__":
	main()
