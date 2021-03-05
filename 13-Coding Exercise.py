#Trim all spaces and newline charactes '\n' from the 'word' variable. Save the result in the 'new_word' variable.

#Expected result:
# hello_world

word = ' h\nel  lo_  \nwor  ld '
new_word = word.replace(' ','').replace('\n','')

print(new_word)

#Output: 'hello_world'
