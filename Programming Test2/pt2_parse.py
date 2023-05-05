# Programming test 2, Part 1, CSC 135 Spring 2023
# Name: Adrian Gonzalez
# Sac State username: AdrianGonzalez

# When you are done, write your name and username above, save, and
# submit this file to
#
#     https://fileinbox.com/csc135/AdrianGonzalez
#
# with xxyxx replaced by your Sac State username.

# Complete the function below following the PDA method
# seen in class for
#      S  -->  aSbS
#      S  -->  lambda
# The function currently has the example code from the online notes, but
# you will need to change it for this problem. Don't forget to add $
# Some simple tests are given below, but you may want to expand on them.
#
# To be eligible for credit your code must have no syntax errors and the
# parse function you write must not print anything.

class scanner:
    # toks[i] must evaluate to the i-th token in the token stream.
    # Assumes toks does not change during parsing
    def __init__(self,toks):
        self._toks = toks
        self._i = 0
    
    # If no more tokens exist or current token isn't s, raise exception.
    # Otherwise pass over the current one and move to the next.
    def match(self,s):
        if (self._i < len(self._toks)) and (self._toks[self._i] == s):
            self._i += 1
        else:
            raise Exception
            
    # If any tokens remain return the current one. If no more, return None.
    def next(self):
        if self._i < len(self._toks):
            return self._toks[self._i]
        else:
            return None

# Input can be any type where len(input) is defined and input[i] yields a
# string (ie, string, list, etc). Raises Exception on error.
# 7.5 points
def parse(input):
    toks = scanner(input)
    stack = ['S']
    while len(stack) > 0:
        top = stack.pop()
        tok = toks.next()
        if top in ('a', 'b'):
            toks.match(top)
        elif top == 'S' and (tok in ('a', 'b')):  # S -> aSbS
            stack.append('S')
            stack.append('b')
            stack.append('S')
            stack.append('a')
        elif top == 'S' and (tok == None or tok in ('a', 'b')):  # S -> lambda
            pass
        else:
            raise Exception
    if toks.next() != None:
        raise Exception

if __name__ == "__main__":
    # Here are strings that should work correctly. Nothing should print.
    parse("")
    parse("ab")
    # Here are strings that should not work correctly. Nothing should print.
    try:
        parse("c")
    except:
        pass     # We expect this, so do nothing
    else:
        print("Error")
    try:
        parse("aa")
    except:
        pass     # We expect this, so do nothing
    else:
        print("Error")
