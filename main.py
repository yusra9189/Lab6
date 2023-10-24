def encode(x):
    res = ""
    for i in x:
        temp = int(i) + 3
        if temp >= 10:
            temp = temp - 10
        res += str(temp)
    return res

# Decoder Function
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        original_digit = str((int(digit) - 3) % 10)
        decoded_password += original_digit
    return decoded_password



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
        if encoded:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}")
        else:
            print("Please encode a password first.")

    if option == 3:
        break


