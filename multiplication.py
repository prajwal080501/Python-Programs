number = (input("Enter number to get its multiplication table:"))#Enter any integer to get is multiplication table upt 10.
number=int(number) #typecasted a string to integer.
for i in range(0,11):#this for loop multiplies the number with i variable which increments from 1 to 10 
    print(number ,'x' ,i , '=' ,i*number ) #this line displays the desired output.
    
