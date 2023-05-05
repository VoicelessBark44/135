# Adrian Gonzalez
# CSC 135 Section 1
# Creates a Recursive Parsing Tree
# As parser recursivly goes through the input and creates a tree as it goes
# through the interpreter provided by the prof will interpret the inout tokens and run the program

# This file contains two support classes followed by parsing code.
# scanner is a simple class that delivers tokens to the parser
# node is a simple class for building trees with any number of children

class scanner:
    # toks[i] must evaluate to the i-th token in the token stream.
    # Assumes toks does not change during parsing
    def __init__(self,toks):
        self._toks = toks
        self._i = 0
    
    # If no more tokens exist or current token isn't s, raise exception.
    # Otherwise, pass over the current one and move to the next.
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

# A tree node is a piece of data along with an optional list of children.
# If the _children field is None it indicates the node is a leaf
class node:
    def __init__(self, data):
        self.data = data
        self.children = None
    
    def add_child(self, child):
        if self.children == None:
            self.children = []
        self.children.append(child)
        
    def is_leaf(self):
        return self.children == None

# parse accepts an indexible squence of strings and succeeds without exception
# if the token sequence is entirely consumed and is in L(S). In the case of Bf
# the input will be a string of characters from <>+-.,[]
def parse(input):
    toks = scanner(input)
    root = parseS(toks)
    if toks.next() != None:
        raise Exception
    return root

# --- DO NOT CHANGE ANY CODE ABOVE THIS LINE ---

# Parser for
# S → CS | LS | λ
# L → [ S ]
# C → > | < | + | - | ,  | .

# Predictor Table
# S -> CS ; > < + - , .
# S -> LS ; [
# S -> lambda ; ] $
# L -> [S] ; [
# C -> > ; >
# C -> < ; <
# C-> + ; +
# C -> - ; -
# C -> , ; ,
# C -> . ; .

# Consumes sequence of tokens in L(S), returns parse tree for it
def parseS(toks):
    tok = toks.next()
    new = node('S')
    if tok in ('>', '<', '+', '-', ',', '.'):  # S -> CS
        new.add_child(parseC(toks))
        new.add_child(parseS(toks))
        #parseC(toks)
        #parseS(toks)
    elif tok == '[': # S -> LS
        new.add_child(parseL(toks))
        new.add_child(parseS(toks))
        #parseL(toks)
        #parseS(toks)
    elif tok == None or tok == ']': # S -> lambda
        new.add_child(node('λ'))
        pass
    else:
        raise Exception
    return new

# Consumes sequence of tokens in L(L), returns parse tree for it
def parseL(toks):
    tok = toks.next()
    new = node('L')
    if tok == '[': # L -> [S]
        toks.match('[')
        new.add_child(node('['))
        new.add_child(parseS(toks))
        #parseS(toks)
        toks.match(']')
        new.add_child(node(']'))
    else:
        raise Exception
    return new

# Consumes sequence of tokens in L(C), returns parse tree for it
def parseC(toks):
    tok = toks.next()
    new = node('C')
    if tok == '>': # C -> >
        toks.match('>')
        new.add_child(node('>'))
    elif tok == '<':  # C -> <
        toks.match('<')
        new.add_child(node('<'))
    elif tok == '+':  # C -> +
        toks.match('+')
        new.add_child(node('+'))
    elif tok == '-':  # C -> -
        toks.match('-')
        new.add_child(node('-'))
    elif tok == ',':  # C -> ,
        toks.match(',')
        new.add_child(node(','))
    elif tok == '.':  # C -> .
        toks.match('.')
        new.add_child(node('.'))
    else:
        raise Exception
    return new

if __name__ == '__main__':
    parse("++,>-<--")