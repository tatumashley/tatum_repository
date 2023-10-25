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

def decode(original_password):
    for i in range(len(original_password)):
        if original_password[i] >=3 and original_password <=9:
            original_password[i] -= 3
        elif original_password[i] == 2:
            original_password[i] = 9
        elif original_password[i] == 1:
            original_password[i] = 8
        elif original_password[i] == 0:
            original_password[i] = 7
    return ''.join(original_password)



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
            decoded_input = decode(encoded_input)
            print(f"The encoded password is {decoded_input}, and the original password is {user_input}.")
        elif menu_option == 3:
            break
        else:
            continue