#fizzbuzz program which prints number for 0 to a number you want it prints the numbers but where there is multiple  of 3 it will print fizz instead of number where there is multiple of 5 it will print buzz where  the number is bot multiple of 3 as well as 5 it prints FizzBuzz.
number = (input("Enter the range you want to print number till:"))#Enter the range till where you want to print the fizzBuzz numbers
number = int(number)#typecasting default str to integer.
for i in range (0,number):#for loop will print numbers from 0 to till the range you have given it to enter.
    if(i%3 == 0 and i%5==0 ): #first if will check whether the entered number is divisible by both 3 and 5 if yes it will print FizzBuzz else will go to next piece of code
        print(str(i), ' :FizzBuzz')
    if(i%3==0):#This if statements check if the number is divisible by 3 if yes it prints Fizz else goes to next piece of code 
        print(str(i), ': Fizz')
    if(i%5==0):
        print(str(i), ': Buzz')#This if statements check if the number is divisible by 5 if yes it prints Buzz and code stops by printing remaining numbers as it is in the range. 
    print(str(i))
