# Public	no1
# Protected	_no2
# Private	__no3

class Base:
	def __init__(self):
		self.no1 = 11		# public member 
		self._no2 = 21		# Protected member
		self.__no3 = 51		# pritvte member

	def Fun(self):			# public method	
		print(self.no1,self._no2,self.__no3)

	def _Fun(self):			# protected method
		print(self.no1,self._no2,self.__no3)
		
	
	def __Fun(self):		# private method
		print(self.no1,self._no2,self.__no3)




class Derived(Base):
	def __init__(self):
		Base.__init__(self)
	def gun(self):
		print(self.no1)
		print(self._no2)
#		print(self.__no3)
		self.Fun()
		self._Fun()
#		self.__Fun()		# Not Allowd	
def main():

	boj = Base()	
	print(boj.no1)
	print(boj._no2)
	#print(boj.__no3)		# Not Allowd
	
	boj.Fun()
	boj._Fun()
	boj.__Fun()			# Not Allowd
	
	dobj = Derived()
	dobj.gun()


if __name__ =="__main__":
	main()

