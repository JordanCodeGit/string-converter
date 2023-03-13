#This is jordan's code

while True:
    # Take input string from user
    input_str = input("Enter a string to convert (or 'exit' to quit): ")
    
    # Exit program if user enters 'exit'
    if input_str == 'exit':
        break
    
    # Display conversion options to the user
    print("============Select a conversion option:=============")
    print("1. Binary")
    print("2. Hexadecimal")
    print("3. Decimal")
    print("4. Octal")
    print("5. ASCII")
    print("")
    
    # Take input option from the user
    option = input("Enter option number: ")
    
    # Convert input string based on user's selected option
    if option == '1':
        binary = ''.join(format(ord(c), '08b') for c in input_str)
        print(f"Binary: {binary}")
    elif option == '2':
        hexadecimal = ''.join(hex(ord(c))[2:] for c in input_str)
        print(f"Hexadecimal: {hexadecimal}")
    elif option == '3':
        decimal = ''.join(str(ord(c)) for c in input_str)
        print(f"Decimal: {decimal}")
    elif option == '4':
        octal = ''.join(oct(ord(c))[2:] for c in input_str)
        print(f"Octal: {octal}")
    elif option == '5':
        ascii_code = ''.join(str(ord(c)) + ' ' for c in input_str)
        print(f"ASCII Code: {ascii_code}")
    else:
        print("Invalid option selected. Please select again.")