# Import our numeral class
from Numeral import Numeral

# Make our two Numerals
numOne = Numeral(4, "x")
numTwo = Numeral(1, "x")

# Add them together (and print it)
print(numOne * numTwo)

# What happens when you print one
print(f"\n{numOne}")
print(numTwo)