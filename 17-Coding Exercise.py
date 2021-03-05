#Get all unique words from the variable 'text' and put them on the list 'list_of_words'. Furthermore,'list_of_words' cannot contain comma ',' and colon ':'.

#Expected result:
#['on', 'sat', 'Dumpty', 'Humpty', 'wall', 'great', 'fall', 'a', 'had']



import re   #re(regular expression) is a library which is used to petrform regular expressions operations in any python program.  

text = 'Humpty Dumpty: sat on a wall, Humpty Dumpty: had a great fall'
list_of_words = list(set(re.split(r',\s|\s|:\s',text)))

print(list_of_words)

#Output: ['on', 'sat', 'Dumpty', 'Humpty', 'wall', 'great', 'fall', 'a', 'had']
