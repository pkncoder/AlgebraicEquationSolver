# Import our numeral class
from Numeral import Numeral

# Make our two Numerals
numOne = Numeral(4)
numTwo = Numeral(2, "x", 6)

# Add them together (and print it)
print(numOne * numTwo)

# What happens when you print one
print(f"\n{numOne}")
print(numTwo)