#Align the value in the 'name' variable to the right and add six underscore character '_'. Save the result in the 'align_right' variable. Use sring formatter.

#Expected result:
#______Mark


name = 'Mark'
align_right = F'{name:_>10}'

print(align_right)

#Output: '______Mark'
