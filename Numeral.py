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

        # Boolean: variable Declares if this is a variable or not
        # Test for a name value first
        if name != None:
            self.variable = True
        
        # If not then set variable to false
        else:
            self.variable = False

            # Also temp adding fullForm here
            self.fullForm = value

        # String: name The vairiable name (such as x) that declares the variable
        # Name is a default of None
        # Test to see if name is none, if it itn's then continue on
        if name != None:

            # Test for name errors
            if len(name) != 1 or name == " ":
                
                # If the name is not formatted, then raise an error
                raise InvalidVariableName("Invalid Name")

            # If no errors occor, then set the variables
            else:

                # Set the name accordingly
                self.name = name

                # Set the full form as the str(value) of the numeral plus the name
                self.fullForm = str(value) + name


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