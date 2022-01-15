# **Reverse a String** - Enter a string and the program will reverse it and
# print it out.

# VERSION 2: This string gets reversed with a recursive function

teststr = "Hi, I'm a string!"

def reverse_string(inputstr):
    if len(inputstr) == 0:
        return inputstr
    else:
        return reverse_string(inputstr[1:]) + inputstr[0]

print(reverse_string(teststr))