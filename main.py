

def get_input_angle():
""" Obtain input from user and convert to an int"""
message = 'Please provide an angle:'
value_as_string = input(message)
while not value_as_string.isnumeric():
print('The input must be an integer!')
value_as_string = input(message)
return int(value_as_string)