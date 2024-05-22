input_string=input("Enter the string here ")
given_char=input("Enter the character here ")

m=lambda input_string, given_char: input_string[0]==given_char if input_string else False
print(m(input_string, given_char))