




name = input("what is your name?")
level = input(
    "Hi " + name + " what level would you like to play? level 1-5?"
)

if level == 1

elif level == 2

elif level == 3 

elif level == 4

else level == 5








def is_only_digits(letter):
    if letter == "":
        return False

    for i in letter:
        if i not in "a b c d e f g h i j k l m n o p q r s t u v w x y z".split():
            return False

    return True