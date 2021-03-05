#Convert the value in the 'number' variable to the following string: 015.9877. Save the result in the 'new_number' variable. Use String Formatter.

#Expeted result:
#015.9877

number = 15.987654321
new_number = f'{number:08.4f}'
print(new_number)


#Output: 015.9877
