def print_factor(number):
   print("the factors of",number,"are:")
   for i in range(1, number + 1):
       if number % i == 0:
           print(i)
number = int(input("enter ur numbe r to find its factor or smthing"))
print_factor(number)