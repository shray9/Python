def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

# Taking input from the user
num = int(input("Enter a number: "))
check_even_odd(num)
