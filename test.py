num = input('Enter any number : ')
try:
    val = int(num)
    if num%2==0:
        print('The given number is Jor')
    else:
        print('The given number is Bijor')
except ValueError:
    print("That's not a valid number, Try Again !")
print("Yeasher Arafath")
