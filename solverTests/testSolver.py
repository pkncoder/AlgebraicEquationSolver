from testSimplifier import simplify

equation = input("Input your equation to simplify it: ")

simpleEquation = simplify(equation)

for numeral in simpleEquation:
    print(numeral)