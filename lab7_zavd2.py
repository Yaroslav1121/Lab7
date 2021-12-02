from numpy import *
import random
import pylab
from collections import Counter


def character_distribution_of_string(pass_string):
  letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  chars_in_string = Counter(pass_string)
  res = {}
  for letter in letters:
    if(letter in chars_in_string):
      res[letter] = chars_in_string[letter]
    else:
      res[letter] = 0
  return(res)


text = input("Enter your sentence: ")
y = list(character_distribution_of_string(text).values())
letters_str = "abcdefghijklmnopqrstuvwxyz"
letters = list(letters_str)
x = letters
fig = pylab.figure()
pylab.bar(x, y, 0.8)
pylab.show()
fig.savefig("saved_figure.jpg", dpi=100)
print(y)
