"""
Numeral class:
    holds any int, float, or variable
"""
class Numeral:
    
    # Initialation code
    def __init__(self, variable, value):
        
        # Boolean: variable Declares if this is a variable or not
        self.variable = variable
        
        # Float: value The amount that your Numeral holds
        self.value = value

