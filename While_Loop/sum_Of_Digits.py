n = int(input("Enter the number\n"))
sum = 0

while n > 0:
    r = n % 10
    n = n // 10
    sum = sum + r

print("The sum of given number is: ", sum)