# Task 1: Check if a Number is Even or Odd
number = int(input('Enter a number: '))

if (number%2) == 0:
    print(number, 'is an even number.')
else:
    print(number, 'is an odd number.')
    
# Task 2: Sum of Integers from 1 to 50 Using a Loop
sum = 0

for i in range(1,51):
    sum += i
print("The sum of numbers from 1 to 50 is:", sum)