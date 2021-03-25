def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    else:
        return input


again = 'y'    

print('\n---------- Welcome to "fizzbuzz" by Kamal ----------\n')

while again == 'y':
    input_num = int(input('Enter your Number : '))
    print('\n',fizz_buzz(input_num),'\n')
    again = input("Try again (yes = y , No = n) : ").lower()
    print('\n')
print('----------- Thank You ---------')
