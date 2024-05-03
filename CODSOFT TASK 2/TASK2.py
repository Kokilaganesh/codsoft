import random
import string

def generate_password(length: int) -> str:
    """Generate a random password with the given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main() -> None:
    """The main function for the Password Generator Application."""
    print("Password Generator Application")
    print("-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=")

    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 8:
            print("Password length should be at least 8 characters.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Generate and display the password
    password = generate_password(length)
    print("\nGenerated Password:")
    print("*" * length)
    print(f"Your password has been saved to the clipboard.")
    import pyperclip
    pyperclip.copy(password)

if __name__ == "__main__":
    main()