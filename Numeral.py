from Exceptions import InvalidVariableName

"""
Numeral class:
    holds any int, float, or variable
"""
class Numeral:
    
    # Initialation code
    def __init__(self, value: float, variable: bool, name: str):
        
        # Float: value The amount that your Numeral holds
        self.value = value

        # Boolean: variable Declares if this is a variable or not
        self.variable = variable

        # String: name The vairiable name (such as x) that declares the variable
        if name != None:
            if len(name) != 1 or name == " ":
                raise InvalidVariableName("Invalid Name")

            else:
                self.name = name
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

                # Return this one's full form plus the other's
                return f"{self.fullForm}+{other.fullForm}"