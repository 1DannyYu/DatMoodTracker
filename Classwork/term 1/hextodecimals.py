"""
Number Conversion App
Converts between Binary, Decimal, and Hexadecimal
"""

def binary_to_decimal(binary_str):
    """Convert Binary to Decimal"""
    try:
        # Remove spaces and validate
        binary_str = binary_str.strip()
        if not all(c in '01' for c in binary_str):
            raise ValueError("Binary must only contain 0s and 1s")
        if not binary_str:
            raise ValueError("Input cannot be empty")
        
        decimal = int(binary_str, 2)
        return decimal
    except ValueError as e:
        return f"Error: {e}"


def decimal_to_binary(decimal_num):
    """Convert Decimal to Binary"""
    try:
        num = int(decimal_num)
        if num < 0:
            raise ValueError("Decimal number must be non-negative")
        
        binary = bin(num)[2:]  # [2:] removes the '0b' prefix
        return binary
    except ValueError:
        return "Error: Please enter a valid integer"


def hexadecimal_to_decimal(hex_str):
    """Convert Hexadecimal to Decimal"""
    try:
        hex_str = hex_str.strip()
        if not hex_str:
            raise ValueError("Input cannot be empty")
        
        decimal = int(hex_str, 16)
        return decimal
    except ValueError:
        return "Error: Please enter a valid hexadecimal number (0-9, A-F)"


def decimal_to_hexadecimal(decimal_num):
    """Convert Decimal to Hexadecimal"""
    try:
        num = int(decimal_num)
        if num < 0:
            raise ValueError("Decimal number must be non-negative")
        
        hexadecimal = hex(num)[2:]  # [2:] removes the '0x' prefix
        return hexadecimal.upper()
    except ValueError:
        return "Error: Please enter a valid integer"


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("Number Conversion App")
    print("="*50)
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Hexadecimal to Decimal")
    print("4. Decimal to Hexadecimal")
    print("5. Exit")
    print("="*50)


def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\n--- Binary to Decimal ---")
            binary_input = input("Enter a binary number (e.g., 1010): ")
            result = binary_to_decimal(binary_input)
            print(f"Binary: {binary_input} = Decimal: {result}\n")
        
        elif choice == "2":
            print("\n--- Decimal to Binary ---")
            decimal_input = input("Enter a decimal number (e.g., 10): ")
            result = decimal_to_binary(decimal_input)
            print(f"Decimal: {decimal_input} = Binary: {result}\n")
        
        elif choice == "3":
            print("\n--- Hexadecimal to Decimal ---")
            hex_input = input("Enter a hexadecimal number (e.g., 2A): ")
            result = hexadecimal_to_decimal(hex_input)
            print(f"Hexadecimal: {hex_input} = Decimal: {result}\n")
        
        elif choice == "4":
            print("\n--- Decimal to Hexadecimal ---")
            decimal_input = input("Enter a decimal number (e.g., 42): ")
            result = decimal_to_hexadecimal(decimal_input)
            print(f"Decimal: {decimal_input} = Hexadecimal: {result}\n")
        
        elif choice == "5":
            print("\nThank you for using the Number Conversion App!")
            print("="*50)
            break
        
        else:
            print("\nError: Please enter a valid choice (1-5)")


if __name__ == "__main__":
    main()
