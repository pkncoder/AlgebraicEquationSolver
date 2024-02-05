# Import our numeral class
from Numeral import Numeral

# Make our two Numerals
numOne = Numeral(14, "x", 3)
numTwo = Numeral(-27)

# Add them together (and print it)
print(numOne + numTwo)

# What happens when you print one
print(f"\n{numOne}")
print(numTwo)