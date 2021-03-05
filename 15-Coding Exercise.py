#Count the number occurances of the character 'g' in the variable 'text'. Save the result in the 'count' variable.

#Expected result:
#5

text = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall,
All the king's horses and all the king's men,
Couldn't put Humpty together again.'''

count = 0
for i in text:
    if i == 'g':
        count +=1
print(count) 

     #or
  
text = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall,
All the king's horses and all the king's men,
Couldn't put Humpty together again.'''

count = text.count('g')
print(count)

#Output: 5
