# **Reverse a String** - Enter a string and the program will reverse it and
# print it out.

def reverse_string(instr):
    inlist = list(instr)
    inlist.reverse()
    reverse_string = ''
    for i, v in enumerate(inlist):
        reverse_string += inlist[i]
    return reverse_string

while True:
    print("Enter a sting and I'll reverse it!\nEnter 'q' to quit.")
    instring = input(">>> ")
    if 'q' in instring:
        break
    print('\n' + reverse_string(instring) + '\n')
