#task 2 
#A prime number is a number that is only divisible by one and itself.
#Write a method that prints out all prime numbers between 1 and 100 
for num in range(2, 100, 1):
    #count = 0
    for i in range(2, (num//2 + 1)):
        if (num % i == 0):
            #count += 1
            break
        else:
            print(num)
            break