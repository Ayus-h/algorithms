import re

email = re.compile(r'[A-Za-z0-9_.]+@[A-Za-z]+\.[a-z]{2,4}')

print(email.findall("My name is Ayush Bhusal and my email address is Bhusalayush@gmail.com. I also like to be called A@g.com."))

replacer = re.compile(r'[A-Z][A-Za-z0-9]*@')
print(replacer.sub("****@","My name is Ayush Bhusal and my email address is Bhusalayush@gmail.com. I also like to be called A@g.com."))

