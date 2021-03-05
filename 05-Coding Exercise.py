#Create the function 'is_palindrome', which checks if a string is palkindrome or not. The function should return True or False.

#What is Palindroem?
#A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome

def is_palindrom(word: str) -> bool:
    return word == word[::-1]


words = ['kajak', 'inni', 'ananas', 'radar']
for word in words:
    if is_palindrom(word):
        print(f'{word} is a palindrom')
    else:
        print(f'{word} is not a palindrom')
        
#Output:  kajak is a palindrom
#         inni is a palindrom
#         ananas is not a palindrom
#         radar is a palindrom
