# Duck Typing
class C:
	def LearnAndCode(self):
		print("Learn C programming")
class CPP:
	def LearnAndCode(self):
		print("Learn CPP programming")

class Golang:
	def LearnAndCode(self):
		print("learn Golang Progrmming")	

class Programmer:
	def Coding(self,language):
		language.LearnAndCode()

cobj =C()
cpobj = CPP()
gobj= Golang()

obj = Programmer()
obj.Coding(cobj)
obj.Coding(cpobj)
obj.Coding(gobj)
