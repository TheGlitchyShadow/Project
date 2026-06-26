for i in range (1,11):
    print(f"23 x {i} = {23*i}")

sum = 0
num = 1
while num <= 10:
    sum = sum + num
    num = num + 1
print(sum)

n = int(input("Enter number of rows"))
for i in range(1,n + 1):
    for j in range(i):
        print("*",end = " ")
    print()

# 1) Take an integer input from the user and store it in a variable.
# a) Convert the input to an integer using `int()`.
# 2) Check if the number is greater than 1.
# a) Prime numbers are always greater than 1.
# 3) If the number is greater than 1, test whether it is prime:
# a) Use a `for` loop to try dividing the number by values from 2 to √number (inclusive).
# - Use `int(number**0.5) + 1` as the loop limit for efficiency.
# b) If the number is divisible by any `i` (remainder is 0), it is NOT prime:
# - Print "not a prime number"
# - Stop the loop using `break`.
# 4) If the loop finishes without finding any divisor (no `break` happens),
# then the number is prime:
# a) Print "is a prime number".
# 5) If the number is less than or equal to 1,
# it is NOT prime:
# a) Print "not a prime number".
s = int(input("Enter a number: "))
if s > 1:
    for i in range(2,int(s**0.5) + 1):
        if s % i == 0:
            print(f"{s} is not a prime number.")
        else:
            print(f"{s} is a prime number.")
else:
    print(f"{s} is not a prime number.")