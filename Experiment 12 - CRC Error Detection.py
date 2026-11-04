# AIM: To implement a Cyclic Redundancy Check (CRC) for error detection.
# ALGORITHM:
# 1. Read the data bits and generator polynomial.
# 2. Append len(generator) - 1 zeros to the data bits.
# 3. Perform modulo-2 division using XOR to calculate the CRC remainder.
# 4. Append the CRC remainder to the original data to form the codeword.
# 5. Read the received codeword and divide it by the same generator.
# 6. If the remainder is all zeros, report no error; otherwise report an error.


def xor_bits(dividend, divisor):
    return ''.join('0' if a == b else '1' for a, b in zip(dividend[1:], divisor[1:]))


def modulo_two_division(dividend, divisor):
    if not divisor or set(divisor) - {'0', '1'} or divisor[0] != '1':
        raise ValueError('Generator must be a binary string beginning with 1.')
    if set(dividend) - {'0', '1'}:
        raise ValueError('Input must contain only binary digits.')

    width = len(divisor)
    if len(dividend) < width:
        raise ValueError('Dividend must be at least as long as the generator.')

    remainder = dividend[:width]
    for bit in dividend[width:]:
        if remainder[0] == '1':
            remainder = xor_bits(remainder, divisor) + bit
        else:
            remainder = xor_bits(remainder, '0' * width) + bit

    if remainder[0] == '1':
        remainder = xor_bits(remainder, divisor)
    else:
        remainder = xor_bits(remainder, '0' * width)
    return remainder


def main():
    data = input('Enter Data Bits: ').strip()
    generator = input('Enter Generator Polynomial: ').strip()
    if not data or set(data) - {'0', '1'}:
        raise ValueError('Data must be a non-empty binary string.')
    if len(generator) < 2 or set(generator) - {'0', '1'} or generator[0] != '1':
        raise ValueError('Generator must contain at least two binary digits and begin with 1.')

    padded_data = data + '0' * (len(generator) - 1)
    crc = modulo_two_division(padded_data, generator)
    codeword = data + crc
    print('CRC Remainder:', crc)
    print('Transmitted Codeword:', codeword)

    received = input('Enter Received Codeword: ').strip()
    if not received or set(received) - {'0', '1'}:
        raise ValueError('Received codeword must be a non-empty binary string.')
    check = modulo_two_division(received, generator)
    print('No Error Detected' if not check.strip('0') else 'Error Detected')


if __name__ == '__main__':
    main()