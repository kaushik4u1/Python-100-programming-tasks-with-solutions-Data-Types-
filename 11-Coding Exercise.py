#Create the function 'is_string_valid', which checks if provided to it string meets the following requirements:

# String cannot be empty
# String does not end up with 'em'
# String contains only lowecase characters
# String cannot contain a space character

def is_string_valid(string: str) -> bool:
    return not string.endswith('em') and string.islower() and  ' ' not in string

sentences = ['abcdef', 'abcdem', 'abcfEd', 'ab cde', 'bbbbbb', '']

for sentence in sentences:
    if is_string_valid(sentence):
        print(f'"{sentence}" is valid')
    else:
        print(f'"{sentence}" is not valid')
        

#Output:  "abcdef" is valid
#         "abcdem" is not valid
#         "abcfEd" is not valid
#         "ab cde" is not valid
#         "bbbbbb" is valid
#         "" is not valid
