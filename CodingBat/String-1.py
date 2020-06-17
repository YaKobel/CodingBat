# 1. Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'

# def hello_name(name):
#   return "Hello " + name + "!"
#
# def hello_name(name):
#   return "Hello {}!".format(name)
#


# 2. Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
#
# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

# def make_abba(a, b):
#   return (a + b) + (b + a)



# 3. Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'

# def make_tags(tag, word):
#   hash_tag = "<{}>".format(tag)
#   hash_tag2 = "</{}>".format(tag)
#   return hash_tag + word + hash_tag2