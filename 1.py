#Write your code below this line ๐

def prime_checker(number):
  for i in range(1, number+1):
    count = 0
    result = number%i
    
    if result ==0:
      count +=1
      if count == 2:
        print("prime number")
      else:
        print("Not a prime number")
  



#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)



