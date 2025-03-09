def convert_number(num):
    if num < 0 or num > 255:
        return "Error: Input number must be between 0 and 255."

    binary = bin(num)[2:].zfill(8)  # Convert to binary and ensure 8 bits
    hexadecimal = hex(num)[2:].upper()  # Convert to hexadecimal

    return binary, hexadecimal

def main():
    num = int(input("Enter a number between 0 and 255: "))
    binary, hexadecimal = convert_number(num)
    print(f"Binary: {binary}")
    print(f"Hexadecimal: {hexadecimal}")

if __name__ == "__main__":
    main()

