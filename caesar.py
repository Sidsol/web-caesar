from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted_str = ''
    for char in text:
        encrypted_str = encrypted_str + rotate_character(char, rot)

    return encrypted_str

def main():
    from sys import argv, exit
    try:
        rotation = int(argv[1])
    except ValueError:    
        print("Usage: python caesar.py n")
        exit()

    user_str = input("Type a message: ")

    print(encrypt(user_str, rotation))

if __name__ == "__main__":
    main()