# Accept N numbers from user and filterout only even numbers from that N numbers.
# After that add 2 in every even number.
# after the addition of 2 perform summation of that modified number.

# Input [1,3,2,4,6,5,4]

# After filter [2,4,6,4]
# after map [4,6,8,6]
# after reduce 24
    
import functools

def main():
    arr = []		# mutuable,order,duplicate,hetroginous,index
    print("Enter number of elements")
    size = int(input())
    
    for i in range(size):
        print("Enter element number :",i+1)
        no = int(input())
        arr.append(no)
        
    print("Your entered data is :",arr)

    newdata = list(filter(lambda no: (no %2 == 0), arr)) 		#newdata = MarvellousFilter(arr)
    print("After filtering data is :",newdata)
    
    newdata1 = list(map(lambda no: no + 2, newdata))  			#newdata1 = MarvellousMap(newdata)
    print("After map data is :",newdata1)

    output = functools.reduce(lambda no1,no2: no1 + no2, newdata1) 	#output = MarvellousReduce(newdata1)
    print("After reduce result is : ",output)
    
if __name__ == "__main__":
    main()
