FIRST_NAME = input('What is your first name? ')
LAST_NAME = input('What is your last name? ')
FAVORITE_COLOR = input('What is your favorite color? ')
FAVORITE_MOVIE = input('What is your favorite movie? ')
FAVORITE_PLANET = input('What is your favorite planet? ')
NUISANCE = input('Am I asking you too many questions (y/n)? ')

print("\nHello %s %s!" % (FIRST_NAME, LAST_NAME), "\n")
print("Your favorite color, movie and planet are: %s, %s, %s" % (FAVORITE_COLOR, FAVORITE_MOVIE, FAVORITE_PLANET), "\n")

if NUISANCE == "y":
    print("Excuse me, but I am NOT a nuisance!\n")
else:
    print("Thank you for obliging my incessant questioning.\n")

print("Is this file __main__???\n")

if __name__ == "__main__":
    print("Yes, __name__ == %s" % __name__)
else:
    print("No, __name__ == %s" % __name__)