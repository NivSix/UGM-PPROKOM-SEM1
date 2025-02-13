print('Hello'.rjust(10))
print('Hello'.rjust(20)) 
print('Hello World'.rjust(20))
print('Hello'.ljust(10)) 
print('Hello'.rjust(20, '*')) 
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))  

spam = ' Hello World '
print(spam.strip()) 

print(spam.lstrip())
print(spam.rstrip()) 

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS')) 

string = "geeks for geeks geeks geeks geeks"
print(string.replace("geeks", "Geeks")) 

string = "geeks for geeks geeks geeks geeks"
print(string.replace("geeks", "GeeksforGeeks", 3))