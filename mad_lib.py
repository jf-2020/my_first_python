# mad_lib.py - this program will interact with the user, asking her to fill in
#            a given madlib
#

# print("Please fill in the blanks below:")
# print("__(name)__'s favorite subject in school is __(subject)__.")

# NAME = input("What is your name? ")
# SUBJECT = input("What is your favorite subject? ")

# print("%s's favorite subject in school is %s." % (NAME, SUBJECT))

NUMBER = input("Enter a number between 1 and 9: ")
NAME = input("What's your name? ")
VERB = input("Give me a verb: ")
NOUN = input("Give me a noun: ")
ADJECTIVE = input("Give me an adjective: ")

s = "%s " % NAME

print(s*int(NUMBER) + "decided to %s a(n) %s %s " % (VERB, ADJECTIVE, NOUN))