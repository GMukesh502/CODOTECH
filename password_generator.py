

import random
import string

def main():
    print("\n*** Random Password Generator ***")
    print("(Ctrl+C to exit at any time)\n")


    while True:
        try:
            length = input("How many characters? (8-20 recommended) ")
            length = int(length)
            if length < 4:
                print("C'mon, at least 4 characters!")
                continue
            if length > 100:
                print("That's too long! Try something reasonable.")
                continue
            break
        except ValueError:
            print("Please enter a number (like 12)")

    print("\nWhat should the password contain?")
    
    def get_choice(prompt):
        while True:
            resp = input(prompt + " [y/n] ").lower()
            if resp in ('y', 'yes', ''):
                return True
            if resp in ('n', 'no'):
                return False
            print("Please type 'y' or 'n'")

    letters = get_choice("Letters (a-z, A-Z)?")
    numbers = get_choice("Numbers (0-9)?")
    symbols = get_choice("Special characters (!@#$ etc)?")

    # Default to all if nothing selected
    if not (letters or numbers or symbols):
        print("\nYou didn't select anything! Using all character types...")
        letters = numbers = symbols = True

    # Build character set
    chars = []
    if letters: chars.extend(string.ascii_letters)
    if numbers: chars.extend(string.digits)
    if symbols: chars.extend(string.punctuation)

    # Generate password
    try:
        password = []
        
        # Ensure at least one of each selected type
        if letters: password.append(random.choice(string.ascii_letters))
        if numbers: password.append(random.choice(string.digits))
        if symbols: password.append(random.choice(string.punctuation))
        
        # Fill remaining spots
        while len(password) < length:
            password.append(random.choice(chars))
        
        # Shuffle and join
        random.shuffle(password)
        final_password = ''.join(password)

        # Display results
        print("\nYour new password is:")
        print(final_password)
        print(f"\nLength: {len(final_password)} characters")
        print("(Don't forget to save it somewhere secure!)")

    except Exception as e:
        print(f"\nOops! Something went wrong: {e}")

if __name__ == "__main__":
    main()