print("Hello World")
myName = "Le Duc Hieu"
print(myName)
myDate = "9/4/2001"
print(myDate)

# nums = []

# nums.append(1.72)
# nums.append(54)
# nums.append('chieu cao, can nang')
# print(nums)

# name = input("Enter your name: ")

# print("hello", name)

# num1 =float( input("Enter num1: "))
# num2 =float( input("Enter num2: "))

# num3 = num1 - num2

# print("Products is: ", num3)


# num1 = 4
# if(num1>12):
#    print("Num1 is good")
# elif(num1>35):
#    print("Num2 is not gooooo....")
# else:
#    print("Num2 is great")


def hello():
    print ("Hello")
    print("hello again")
hello()
hello()

def getInteger():
   result = int(input("Enter integer: "))
   return result
  
def Main():
   print("Started")
  
   # calling the getInteger function and 
   # storing its returned value in the output variable
   output = getInteger()    
   print(output)
  
# now we are required to tell Python 
# for 'Main' function existence
if __name__=="__main__":
    Main()
