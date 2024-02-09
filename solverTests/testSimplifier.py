from NumeralPack.Numeral import Numeral
import re

def simplify(equation):
    
    # Step one: split up the equation to a series of tokens
    tokenList = splitEquation(equation)
    
    # Step two, parse all the way through the equation to simplify everything
    #simplifiedEquation = solveIplyEquation(tokenList)

    return tokenList

def splitEquation(equation):
    # Clarify some variables to save data
    tempStr = ""
    tokenList = []

    # This variable is a list of every character in the equation string
    equationList = list(equation)

    # Make a large for loop to go over every character
    for char in equationList:

        # Skip over whitespace
        if char == " ":
            pass

        # Check to see if it is the last character in the string
        elif char == equation[-1]:

            # Add the current char to tempstr
            tempStr += char

            # Split tempstr into token list
            tokenList += [tempStr]

            # Reset tempstring
            tempStr = ""

        # Check if it's a number or letter
        elif re.findall(r"[a-zA-Z1-9]", str(char)):

            # If it is then add it to temp string
            tempStr += str(char)

        # Next, see if it is an opporation
        elif re.findall(r"[+-/*^]", char):
            
            # Split tempstr into token list
            tokenList += [tempStr]

            # Reset tempstring
            tempStr = ""

            # Add this opporation
            tokenList += [char]
    
    # Return our final token list
    return tokenList