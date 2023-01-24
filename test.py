import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_letters = []
    password_numbers = []
    password_symbols = []
    for x in range(5):
        gg = random.choice(letters)
        password_letters.append(gg)

    for y in range(4):
        gg = random.choice(numbers)
        password_numbers.append(gg)

    for z in range(3):
        gg = random.choice(symbols)
        password_symbols.append(gg)
    new = password_letters + password_numbers + password_symbols
    random.shuffle(new)

    print(''.join(new))
    # xx = ' '.join(newpass)
    # print(xx)
    # password_entry.config(textvariable=newpass)


generate_password()