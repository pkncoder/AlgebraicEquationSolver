# This is for custom errors
from Exceptions import InvalidVariableName

"""
Numeral class: holds any number, or variable
"""
class Numeral:
    
    # TODO: Make the init code make more sense and compress it a bit
    # Initialation code
    def __init__(this, value: float, name: str=None, exponent: int=1):
        
        # Float: value The amount that your Numeral holds
        this.value = value

        # Start testing for what to set variable, fullform, and name as
        # Start to see if there is a variable in the first place
        if name != None:

            # Test to see if name has any errors
            if len(name) != 1 or name == " ":
                
                # If there is an error, raise an invalid var name exception
                raise InvalidVariableName("Invalid Name")

            # If there are no errors
            else:

                # Int: exponent The current exponent that your Numeral and variable has
                this.exponent = exponent

                # Boolean: variable Says if this Numeral is a variabole or not (V/F)
                this.variable = True
                
                # String: name The clarifier that the variable is followed by (such as x or t)
                this.name = name
                
                # String: fullForm The main/usual form of this Numeral
                # Made by taking the string of value and adding on name ex. 3x, -93t
                # Also think about exponent, because that is in the form too
                if exponent > 1:

                    # The value plus the var name plus a carrot with the exponent
                    this.fullForm = str(value) + name + "^" + exponent
                
                # If the exponent is not one, then add the carrot
                else:

                    # Value plus the var name
                    this.fullForm = str(value) + name


        # If there isn't a var name
        else:

            # Boolean: variable Says if this Numeral is a variabole or not (V/F)
            this.variable = False
            
            # Float: fullForm The main form of this Numeral
            this.fullForm = value
    

    # When you add one Numeral to another
    def __add__(this, other):
        
        # The way this works is by checking for every case, and handalling them approporitly
        # If neither Numeral is a variable 
        if not this.variable and not other.variable:
            
            # This is a very simple thing, just return one value plus the other one
            return this.value + other.value

        # If this Numeral is a variable, but not the other
        elif this.variable and not other.variable:
            
            # Basicly the same as previos, just add on this one's variable name
            # Make this value + other value a string for saftey
            return str(this.value + other.value) + this.name

        # If this Numeral is not a variable, but the other one is
        elif not this.variable and other.variable:
            
            # Same as before but other.name
            return str(this.value + other.value) + other.name

        # Finally, if BOTH Numerals are variables
        else:
            
            # This is when things start to get difficult
            # The main problem when it comes to this is two things
            # Variable names
            # Exponent values
            # Start by checking to see if both names are the same and both exponents are the same
            # Basic case
            # if this.name == other.name and this.exponent == other.exponent:
            pass