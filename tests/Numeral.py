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
                if exponent != 1:

                    # The value plus the var name plus a carrot with the exponent
                    this.fullForm = str(value) + name + "^" + str(exponent)
                
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
            # Return it as a new Numeral so we can use it later
            return Numeral(this.value + other.value)

        # If this Numeral is a variable, but not the other
        elif this.variable and not other.variable:
            
            # Return this full form + other var
            return this.fullForm + "+" + str(other.value)

        # If this Numeral is not a variable, but the other one is
        elif not this.variable and other.variable:
                
            # Same as before but other.name
            return str(this.value) + "+" + other.fullForm


        # Finally, if BOTH Numerals are variables
        else:
            
            # This is when things start to get difficult
            # The main problem when it comes to this is two things
            # Variable names
            # Exponent values
            # Start by checking to see if both names are the same and both exponents are the same
            # Basic case: just add the constants, and keep everything else the same
            if this.name == other.name and this.exponent == other.exponent:

                # Test to see if the exponent is one or not, because we don't need it if it is
                if this.exponent == 1:

                    # Numeral(string of values added plus the var name)
                    return Numeral(this.value + other.value, this.name)

                # If it isn't one, then do the fancy carrot stuff
                else:

                    # Numeral(string (Values) add + this var name + this string (exponent))
                    return Numeral(this.value + other.value, this.name, this.exponent)
                
            # Now that I'm thinking about this, it might not be so crazy
            else:

                # If the names OR the exponents aren't the same, then they have to be seperated anyways
                # So just return both fullForms
                # But also check for negitive num stuff
                # No re-formatting
                if other.value >= 0:
                    
                    # Return this full form plus the other one
                    # Put it in an f-string so it doesn't look so weird
                    return f"{this.fullForm}+{other.fullForm}"
                
                # Re-forrmating IS needed because of a negitive number
                else:

                    # Return this one "minus" the other one
                    # This is done by just using the minus sign from the other.value as our opporator
                    return f"{this.fullForm}{other.fullForm}"
                
    
    # When you subtract one Numeral to another
    # *this is basicly just a copy of __add__
    def __sub__(this, other):
        
        # The way this works is by checking for every case, and handalling them approporitly
        # If neither Numeral is a variable 
        if not this.variable and not other.variable:
            
            # This is a very simple thing, just return one value minus the other one
            # Return it as a new Numeral so we can use it later
            return Numeral(this.value + other.value)

        # If this Numeral is a variable, but not the other
        elif this.variable and not other.variable:
            
            # Just return as it is
            return this.fullForm + "-" + str(other.value)

        # If this Numeral is not a variable, but the other one is
        elif not this.variable and other.variable:
            
            # Return as it is
            return str(this.value) + "-" + other.fullForm

        # Finally, if BOTH Numerals are variables
        else:
            
            # This is when things start to get difficult
            # The main problem when it comes to this is two things
            # Variable names
            # Exponent values
            # Start by checking to see if both names are the same and both exponents are the same
            # Basic case: just add the constants, and keep everything else the same
            if this.name == other.name and this.exponent == other.exponent:

                # Test to see if the exponent is one or not, because we don't need it if it is
                if this.exponent == 1:

                    # Numeral(string of values minus plus the var name)
                    return Numeral(this.value - other.value, this.name)

                # If it isn't one, then do the fancy carrot stuff
                else:

                    # Numeral(string (Values) minus + this var name + this string (exponent))
                    return Numeral(this.value - other.value, this.name, this.exponent)
                
            # Now that I'm thinking about this, it might not be so crazy
            else:

                # If the names OR the exponents aren't the same, then they have to be seperated anyways
                # So just return both fullForms
                # But also check for negitive num stuff
                # No re-formatting
                if other.value >= 0:
                    
                    # Return this full form minus the other one
                    # Put it in an f-string so it doesn't look so weird
                    return f"{this.fullForm}-{other.fullForm}"
                
                # Re-forrmating IS needed because of a negitive number
                else:

                    # This part is a bit weird
                    # Return each full form with the minus taken out of other (the value isn't modified)
                    # Add a + in the middle since its the same as a --
                    # Remove just the plus, so start from index 1 and go onwards
                    return f"{this.fullForm}+{other.fullForm[1:]}"
                

    # Multiplication one numeral by another
    # I am sooooo excited
    def __mul__(this, other):
        
        # Well, its the same thing as previously
        # Break it up into different cases on what is a variable and what isn't

        # Start
        # If neither is a variable
        if not this.variable and not other.variable:
            
            # This var value times the other
            return Numeral(this.value * other.value)

        # If this one is a variable, but the other one isn't
        elif this.variable and not other.variable:
            
            # Check for exponent stuff
            # If it is equal to one, no fance stuff needs to be done (oo that rymes)
            if this.exponent == 1:

                # Values times eachother, add on this var name
                return Numeral((this.value * other.value), this.name)
            
            # But if the exponent DOES need to be shown
            else:
                
                # Values times eachother, add on this var name, add on this var exponent
                return Numeral((this.value * other.value), this.name, this.exponent)

        # If the other one is a variable and this one isn't
        elif not this.variable and other.variable:
            
            # no Exponenet stuff
            if other.exponent == 1:

                # Values timees eachother, but add on the OTHER var name
                return Numeral((this.value * other.value), other.name)
            
            # If exponenet stuff IS needed
            else:

                # Values, timesed, other name, other exponent
                return Numeral((this.value * other.value), other.name, other.exponent)

        # If BOTH are variables
        else:
            
            # Test for if the two of the variables can even go together
            if this.name == other.name:

                # If they can then start to multiply them
                # First, multiply the constants together
                # Then grab this one's name
                # Then add the exponents
                return Numeral((this.value * other.value), this.name, (this.exponent + other.exponent))

            # If they can't then just return them multipling eachother
            else:

                # Return each's full form multipling
                return this.fullForm + "*" + other.fullForm
    
    # Finally, time for deviding
    def __div__(this, other):
        
        # Start getting all the cases
        # Both normal nums
        if not this.variable and not other.variable:
            pass

        # This one var, other not
        elif this.variable and not other.variable:
            pass

        # This one not, other is
        elif not this.variable and other.variable:
            pass

        # Both are variables
        else:

            # If they are able to combine
            if this.name == other.name:
                pass

            # If they can't
            else:
                pass
        


    # When a numeral is printed
    def __str__(this):

        # Just return the full form (string)
        return str(this.fullForm)