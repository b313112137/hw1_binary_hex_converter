def convert_number(num):
    if num < 0 or num > 255:
        return "Error: Input number must be between 0 and 255.", ""

    x = num
    # Convert to binary by checking from the highest power of 2
    binary = ""
    for i in range(7, -1, -1):  # From 2^7 down to 2^0
        if x >= 2**i:
            binary += "1"
            x -= 2**i  # Subtract the corresponding power of 2
        else:
            binary += "0"
     
    first_half = binary[:4]  # Take the first four bits
    second_half = binary[4:] # Take the last four bits
    hex1 = hex(int(first_half, 2))[2:].upper()
    hex2 = hex(int(second_half, 2))[2:].upper()
    hexadecimal = hex1 + hex2

    return binary, hexadecimal  # Return binary and hexadecimal results

def main():
    num = int(input("Enter a number between 0 and 255: "))
    binary, hexadecimal = convert_number(num)
    print(f"Binary: {binary}")
    print(f"Hexadecimal: {hexadecimal}")

if __name__ == "__main__":
    main()
