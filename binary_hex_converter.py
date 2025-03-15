def binary_to_decimal(four_bits):
    decimal_value = 0
    for i in range(4):
        decimal_value += int(four_bits[i]) * (2 ** (3 - i))  
    return decimal_value

def decimal_to_hex(decimal):
    hex_map = "0123456789ABCDEF" 
    return hex_map[decimal]

def convert_number(num):
    if num < 0 or num > 255:
        return "Error: Input number must be between 0 and 255.", ""

    x = num
    binary = ""
    for i in range(7, -1, -1):  
        if x >= 2**i:
            binary += "1"
            x -= 2**i 
        else:
            binary += "0"
    first_half = binary[:4]
    second_half = binary[4:]

    decimal1 = binary_to_decimal(first_half)
    decimal2 = binary_to_decimal(second_half)

    hex1 = decimal_to_hex(decimal1)
    hex2 = decimal_to_hex(decimal2)

    hexadecimal = hex1 + hex2

    return binary, hexadecimal

def main():
    num = int(input("Enter a number between 0 and 255: "))
    binary, hexadecimal = convert_number(num)
    print(f"Binary: {binary}")
    print(f"Hexadecimal: {hexadecimal}")

if __name__ == "__main__":
    main()
