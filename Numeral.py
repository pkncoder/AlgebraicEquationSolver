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

    # When you add 2 Numerals together
    def __add__(self, other):
        
        # Test to see if one of them is a variable or not
        # If both are not, then normally add
        if (not self.variable and not other.variable):
            
            # Return this numeral's value plus another numeral's value
            return self.value + other.value

        # If this Numeral is a var, but not the other one
        elif (self.variable and not other.variable):
            
            # Return this numeral's value plus the other's, and add on this one's name
            return f"{self.value + other.value}{self.name}"
        
        # If the other Numeral is a var, but this is not
        elif (not self.variable and other.variable):
            
            # Return this numeral's value plus the other's, and add on this one's name
            return f"{self.value + other.value}{other.name}"
        
        # Finally, if BOTH Numerals are vars
        else:

            # Test to see if both var names are the same
            # If they are, then add the values together and give this one's name
            if (self.name == other.name):
                
                # Add both values together, then return this var name
                return f"{self.value + other.value}{self.name}"

            # Else, if they aren't the same, just print them adding eachother
            else:

                # Test to see if the numbers are positive or not
                if (other.value >= 0):
                    
                    # If they are then use a + in the middle of them
                    # Return this one's full form plus the other's
                    return f"{self.fullForm}+{other.fullForm}"
                
                # If they are not however, then exchange the plus for a minus
                else:

                    # Return this one's full form minus the other's
                    # The minus comes from the other one's value
                    return f"{self.fullForm}{other.fullForm}"


    # Subtraction is basicly the same thing as addition just a dif. sign
    def __sub__(self, other):
        
        # Test to see if one of them is a variable or not
        # If both are not, then normally subt
        if (not self.variable and not other.variable):
            
            # Return this numeral's value minus another numeral's value
            return self.value - other.value

        # If this Numeral is a var, but not the other one
        elif (self.variable and not other.variable):
            
            # Return this numeral's value minus the other's, and add on this one's name
            return f"{self.value - other.value}{self.name}"
        
        # If the other Numeral is a var, but this is not
        elif (not self.variable and other.variable):
            
            # Return this numeral's value minus the other's, and add on this one's name
            return f"{self.value - other.value}{other.name}"
        
        # Finally, if BOTH Numerals are vars
        else:

            # Test to see if both var names are the same
            # If they are, then subt. the values together and give this one's name
            if (self.name == other.name):
                
                # Sub both values together, then return this var name
                return f"{self.value - other.value}{self.name}"

            # Else, if they aren't the same, just print them subtracting eachother
            else:

                # Test to see if the numbers are positive or not
                if (other.value >= 0):
                    
                    # If they are then use a - in the middle of them
                    # Return this one's full form minus the other's
                    return f"{self.fullForm}-{other.fullForm}"
                
                # If they are not however, then exchange the minus for a plus
                else:

                    # Return this one's full form plus the other's
                    # Get rid of the minus sign when printing, still there in the var tho
                    return f"{self.fullForm}+{other.fullForm[1:]}"
    
    # When a Numeral is printed just return the full form
    def __str__(self):

        # If it isn't a variable, then it just prints the value (look at __init__)
        return str(self.fullForm)