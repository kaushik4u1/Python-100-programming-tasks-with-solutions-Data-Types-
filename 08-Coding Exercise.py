#Add two underscore character '_' before and after the value in the 'name' variable. Save the result in the 'align_center' variable. Use string formatter.

#Expected result:
#___Mark___

name = 'Mark'
align_center =f'{name:_^8}'

print(align_center)

#Output: '__Mark__'
