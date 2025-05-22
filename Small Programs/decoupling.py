# Decoupling Example in Python

feet_inches = input("Enter feet and inches: ")

def parse(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches   # Returns a tuple which includes feet and inches in float type

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
#   return f"{feet} feet and {inches} inches is equal to {meters} meters."

# feet_inches_tuple = parse(feet_inches)
# print("fi", feet_inches_tuple)
# result = convert(feet_inches_tuple[0], feet_inches_tuple[1])

f, i = parse(feet_inches)
result = convert(f, i)
print(f"{f} feet and {i} inches is equal to {result} meters.")

if result < 1:
    print("Kid is too small to use the slide.")
else:
    print("kid can use the slide.")