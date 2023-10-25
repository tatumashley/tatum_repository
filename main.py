def encode(password):
    encoded_list = []
    for element in password:
        element = int(element)
        if element < 7:
            element += 3
        elif element == 7:
            element = 0
        elif element == 8:
            element = 1
        elif element == 9:
            element = 2
        else:
            continue

        encoded_list.append(element)

    return encoded_list

def decode():



if __name__ == '__main__':

    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu_option = input("Please enter an option: ")
        if menu_option == 1:
            user_input = input("Please enter your password to encode: ")
            encoded_input = encode(user_input)
            print("Your password has been encoded and stored!")
        elif menu_option == 2:
            decoded_input = decode(user_input)
            print(f"The encoded password is {decoded_input}, and the original password is {user_input}.")
        elif menu_option == 3:
            break
        else:
            continue