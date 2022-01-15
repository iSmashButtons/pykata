# Count Words in a String: Counts the number of individual words in a string.
# For added complexity read these strings in from a text file and generate a
# summary.

def countwords(instrs: list):
    """ Splits the input string `instr` into a list of words. Returns the length
    of this list. Words are delimited by spaces."""
    assert type(instrs) == list, f"Prameter `instr` should be a list of only strings."

    for i in instrs:
        yield len(i)



with open('./text/countWords/test.md') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.replace('\n', '')

    totalWords = sum(countwords(lines))
    print(f"The file has a total of {totalWords} words.")