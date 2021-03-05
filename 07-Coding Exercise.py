#Align the value in the 'name' variable to the left and add six undescore character '_'. Save the result in the 'align_left' variable. Use string formatter.

#Expected result:
#Mark______

name = 'Mark'
align_left =  F'{name:_<10}'

print(align_left)


#Output: 'Mark______'
