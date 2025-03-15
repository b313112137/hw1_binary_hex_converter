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
    def binary_to_decimal(four_bits):
        return (int(four_bits[0]) * (2**3) +
                int(four_bits[1]) * (2**2) +
                int(four_bits[2]) * (2**1) +
                int(four_bits[3]) * (2**0))

    hex1 = hex(binary_to_decimal(first_half))[2:].upper()
    hex2 = hex(binary_to_decimal(second_half))[2:].upper()
    hexadecimal = f"{hex1}{hex2}"
    return binary, hexadecimal 

def main():
    num = int(input("Enter a number between 0 and 255: "))
    binary, hexadecimal = convert_number(num)
    print(f"Binary: {binary}")
    print(f"Hexadecimal: {hexadecimal}")

if __name__ == "__main__":
    main()
