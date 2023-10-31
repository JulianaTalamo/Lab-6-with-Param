# this is my first github addition

# Juliana Talamo main.py for Lab 6

def encode(password):
    password_list = list(password)
    encoded_list = []
    for i in password_list:
        encoded_list.append(str((int(i) + 3) % 10))
    encoded_password = ''.join(encoded_list)
    return encoded_password

def decode(encoded_password):
    return_str = ''
    for digit in encoded_password:
        digit = int(digit)
        return_str += str((digit + 7) % 10)
    return return_str

def menu():
    password = None
    encoded_result = None

    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        try:
            option = int(input("Please enter an option: "))
        except:
            print("That is not an available option. Please enter a number, 1-3. ")
            continue

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_result = encode(password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            decoded_result = decode(encoded_result)
            print(f"The encoded password is {encoded_result}, and the original password is {decoded_result}")

        elif option == 3:
            print("Quitting program")
            break

        else:
            print("That is not an available option. Please enter a number, 1-3. ")
            continue


if __name__ == "__main__":
    menu()
