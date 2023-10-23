def encode(x):
    for i in x:
        i = int(i) + 3
        if i >= 10:
            i = i - 10
        print(i, end='')
    return ''

def decode(x):
    pass


while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print('\n')

    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
    print("Your password has been encoded and stored!")
    print()

    if option == 2:
        pass

    if option == 3:
        break