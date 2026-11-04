# AIM:
# To implement an error detection code using Cyclic Redundancy Check (CRC).
#
# ALGORITHM:
# 1. Accept the data bits and generator polynomial from the user.
# 2. Append (generator length - 1) zeros to the data bits.
# 3. Perform modulo-2 division using XOR operations.
# 4. Append the remainder to the original data to form the transmitted codeword.
# 5. Accept the received codeword from the user.
# 6. Divide the received codeword by the same generator polynomial.
# 7. If the remainder is all zeros, report that no error is detected; otherwise report an error.

def xor(dividend, divisor):
    return "".join(
        "0" if dividend[index] == divisor[index] else "1"
        for index in range(1, len(divisor))
    )


def mod2div(dividend, divisor):
    if not dividend or not divisor or set(dividend + divisor) - {"0", "1"}:
        raise ValueError("Data and generator must contain only binary digits.")
    if len(divisor) < 2 or divisor[0] != "1":
        raise ValueError("Generator polynomial must start with 1 and contain at least 2 bits.")
    if len(dividend) < len(divisor):
        raise ValueError("Dividend must be at least as long as the generator.")

    width = len(divisor)
    remainder = dividend[:width]

    for bit in dividend[width:]:
        if remainder[0] == "1":
            remainder = xor(remainder, divisor) + bit
        else:
            remainder = xor(remainder, "0" * width) + bit

    if remainder[0] == "1":
        remainder = xor(remainder, divisor)
    else:
        remainder = xor(remainder, "0" * width)

    return remainder


def main():
    data = input("Enter Data Bits: ").strip()
    key = input("Enter Generator Polynomial: ").strip()

    try:
        if not data or set(data) - {"0", "1"}:
            raise ValueError("Data must contain only binary digits.")

        appended_data = data + "0" * (len(key) - 1)
        remainder = mod2div(appended_data, key)
        codeword = data + remainder

        print("\nCRC Remainder:", remainder)
        print("Transmitted Codeword:", codeword)

        received = input("\nEnter Received Codeword: ").strip()
        if not received or set(received) - {"0", "1"}:
            raise ValueError("Received codeword must contain only binary digits.")

        check = mod2div(received, key)
        if check == "0" * len(check):
            print("No Error Detected")
        else:
            print("Error Detected")
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
