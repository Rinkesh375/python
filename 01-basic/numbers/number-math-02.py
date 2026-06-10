import math


print(math.floor(3.14))


print(math.floor(-3.14))


#"Truncate" = "chop off or remove the decimal part"
print(math.trunc(100.01))
print(math.trunc(-100.01))


print((1+2j)*6)

x = 3 + 4j

print(x.real)
print(x.imag)





# hex() converts a decimal number to hexadecimal (base 16)
# 0x prefix means the value is hexadecimal
print(hex(8))      # Output: 0x8

# oct() converts a decimal number to octal (base 8)
# 0o prefix means the value is octal
print(oct(8))      # Output: 0o10

# bin() converts a decimal number to binary (base 2)
# 0b prefix means the value is binary
print(bin(8))      # Output: 0b1000