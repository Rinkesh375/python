# float uses binary representation
# Some decimal numbers (0.1, 0.2, 0.3) cannot be stored exactly
# This causes tiny rounding errors

print(0.1 + 0.1 + 0.1 - 0.3)

# Decimal stores decimal values exactly
# Useful for money, banking, financial calculations

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))



print(type(True))



print(type(5))

print(type("Rinkesh"))


print(type([]))