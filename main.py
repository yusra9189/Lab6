def encode(x):
    res = ""
    for i in x:
        temp = int(i) + 3
        if temp >= 10:
            temp = temp - 10
        res += str(temp)
    return res

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
        encoded = encode(password)
    print("Your password has been encoded and stored!")


    if option == 2:
        print(f"The encoded password is {encoded}")

    if option == 3:
        break


