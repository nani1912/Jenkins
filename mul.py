# Python Program - Print Multiplication Table of a Number

print("Enter 'x' for exit.");
#num = input("Enter a number: ");

num = 10
if num == 'x':
    exit();
else:
    number = int(num);
    for i in range(1, 11):
        print(number, "*", i, "=", number*i);
