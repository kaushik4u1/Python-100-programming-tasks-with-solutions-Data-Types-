#Create the variable 'full_namer_str' which contains values assigned in the dictionary keys 'full_name_dict'. Values should be seperated by a space.Use string formatter.

#Expected Result:
#Alice Smith

full_name_dict = {
    'first_name': 'Alice',
    'last_name': 'Smith'
}

full_name_str = '{first_name} {last_name}'.format(**full_name_dict)


#Output: 'Alice Smith'
