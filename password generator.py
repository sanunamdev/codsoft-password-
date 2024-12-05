import random
import string

def generate_password(length=12):
    # Define possible characters for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the available pool
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Ask the user for the desired password length
def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length (default is 12): "))
    except ValueError:
        print("Invalid input! Using default length of 12.")
        length = 12
    
    # Generate the password
    password = generate_password(length)
    
    print(f"Generated Password: {password}")

# Run the program
if __name__ == "__main__":
    main()
