




name = input("what is your name?")
level = int(input(
    "Hi " + name + " what level would you like to play? level 1-3?"
))

if level == 1:
    noun_1 = input("Once upon a time in the great land of your noun ") 
    print(f'''Once upon a time in the great land of {noun_1}, 
    In this {adjective_1} kingdom there was a great witch whos name was {noun_2}. 
    She had a {adjective_2} smile and {adjective_3} hair. One day she was brewing her potions she heard a {onomatopoeia_1}.
    she ran outside and saw one of her cats {noun_3}."curse you" she yelled to the sky and she ran to get her broom and {object_1}.
    She was heading towards the {monster_1} civilization when suddenly she got knocked out of the sky.
    she fell towards the ground and heard her bones ({onomatopoeia_2}.
    She limped over behind a tree and felt her heart {adjective_4}.
    A snapping of {noun_4} came from the bushes on her left.
    Her eyes dialated in fear and she started breathing harder as the {adjective_5} beast came out of the bushes.
    But it was just a {adjective_6}{animal_1}. She took {animal_1} home and they lived happily ever after.''')
elif level == 2:
    print(f'''The {adjective_1} door opened with a loud creak. The first thing I see is a big {adjective 2} {noun1} ''')
elif level == 3:
    print(f'''  ''')
else:
    level = input;"please choose level through 5"








def is_only_letters(letter):
    if letter == " ":
        return False

    for i in letter:
        if i not in "a b c d e f g h i j k l m n o p q r s t u v w x y z".split():
            return False
        return True