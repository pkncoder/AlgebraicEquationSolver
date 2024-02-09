from NumeralPack.Numeral import Numeral
import re

def simplify(equation):
    
    # Step one: split up the equation to a series of tokens
    tokenList = splitEquation(equation)
    
    # Step two, parse all the way through the equation to simplify everything
    simplifiedEquation = solveIplyEquation(tokenList)

    return tokenList

def splitEquation(equation):
    # Clarify some variab   les to save data
    tempStr = ""
    tokenList = []

    # Make a large for loop to go over every character
    for i in range(len(equation)):

        # Skip over whitespace
        if i == " ":
            pass

        # Check if it's a number or letter
        if re.search(r"[a-zA-Z1-9]", i):

            # If it is then add it to temp string
            tempStr += i
    
    return tempStr