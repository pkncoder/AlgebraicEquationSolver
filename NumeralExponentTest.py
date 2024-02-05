# This is for custom errors
from Exceptions import InvalidVariableName

"""
Numeral class: holds any number, or variable
"""
class Numeral:
    
    # TODO: Make the init code make more sense and compress it a bit
    # Initialation code
    def __init__(self, value: float, name: str=None):
        
        # Float: value The amount that your Numeral holds
        self.value = value

        # Start testing for what to set variable, fullform, and name as
        # Start to see if there is a variable in the first place
        if name != None:

            # Test to see if name has any errors
            if len(name) != 1 or name == " ":
                
                # If there is an error, raise an invalid var name exception
                raise InvalidVariableName("Invalid Name")

            # If there are no errors
            else:

                # Boolean: variable Says if this Numeral is a variabole or not (V/F)
                self.variable = True
                
                # String: name The clarifier that the variable is followed by (such as x or t)
                self.name = name
                
                # String: fullForm The main/usual form of this Numeral
                # Made by taking the string of value and adding on name ex. 3x, -93t
                self.fullForm = str(value) + name

        # If there isn't a var name
        else:

            # Boolean: variable Says if this Numeral is a variabole or not (V/F)
            self.variable = False
            
            # Float: fullForm The main form of this Numeral
            self.fullForm = value