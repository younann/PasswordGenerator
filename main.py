import random, string


def main():
    print("Welcome to PassGen ....")
    print("Please chose from each section yes or no to include...")
    numbers = input("Do you want numbers in your password: ")
    char = input("Do you want character in your password: ")
    schar=input("Do you want special characters in your password :")
    print("please Wait....")
    passchar = None
    if numbers == 'yes' and char == 'yes' and schar=='yes':
        passchar = string.digits + string.ascii_letters +string.punctuation
    if numbers == 'no':
        passchar = string.ascii_letters +string.punctuation
    if char == 'no':
        passchar = string.digits + string.punctuation
    if schar=='no':
        passchar=string.digits+string.ascii_letters
    password = []
    len = random.randint(10, 50)
    for i in range(len):
        password.append(random.choice(passchar))
    password_to_return=''.join(password)

    print('Here is your Password: {}'.format(password_to_return))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
