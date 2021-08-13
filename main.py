from NumbersApi import NumbersApi
print("Enter a number or write 'r' for a random fact.")
while True:
    number = input()
    if number != 'r':
        try:
            number = int(number)
        except ValueError:
            print("it is not a number or even an 'r'. Try again.")
        else:
            print(NumbersApi().get_number_fact(number))
            break
    else:
        print(NumbersApi().get_random_number_fact())





