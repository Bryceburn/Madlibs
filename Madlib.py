




name = input("what is your name?")
level = int(input(
    "Hi " + name + " what level would you like to play? level 1-3?"
))

if level == 1:
    noun_1 = input("Once upon a time in the great land of _____ ") 
    adjective_1 = input("In this _____ kingdom,")
    noun_2 = input("there was a great witch whos name was _____")
    adjective_2 = input("She had a _____ smile")
    adjective_3 = input("and ____ hair")
    onomatopoeia_1 = input("One day she was brewing her potions she heard a _____")
    noun_3 = input("She ran outside and saw one of her cats ____")
    object_1 = input("'Curse you' she yeled to the sky and she ran to get her broom and _____")
    monster_1 = input("She was heading towards the _____ civilization when suddenly she got knocked out of the sky")
    onomatopoeia_2 = input("She fell towards the ground and heard her bones _____")
    adjective_4 = input("She limped over behind a tree and felt her heart _____")
    noun_4 = input("A snapping of _____ came from the bushes on her left")
    adjective_5 = input("Her eyes dilated in fear and she started breathing harder as the _____ beast came out of the bushes")
    adjective_6 = input("but it was just a ______")
    animal_1 = input(f"but it was just a {adjective_6} _____")
    print(f'''Once upon a time in the great land of {noun_1}, 
    In this {adjective_1} kingdom there was a great witch whos name was {noun_2}. 
    She had a {adjective_2} smile and {adjective_3} hair. One day she was brewing her potions she heard a {onomatopoeia_1}.
    She ran outside and saw one of her cats {noun_3}."curse you" she yelled to the sky and she ran to get her broom and {object_1}.
    She was heading towards the {monster_1} civilization when suddenly she got knocked out of the sky.
    she fell towards the ground and heard her bones ({onomatopoeia_2}.
    She limped over behind a tree and felt her heart {adjective_4}.
    A snapping of {noun_4} came from the bushes on her left.
    Her eyes dilated in fear and she started breathing harder as the {adjective_5} beast came out of the bushes.
    But it was just a {adjective_6}{animal_1}. She took {animal_1} home and they lived happily ever after.''')
elif level == 2:
    print(f'''The {adjective_1} door opened with a loud creak. The first thing I see is a big {adjective_2} body.
          The wall is covered in {noun_1}. A {sound_1} rang through the halls.
           As I walk through the halls I get the feeling that {sentance_1}. I spin around and from the dark {object_1} appears.
           I scream and run as fast as I can but it is catching up, I see and {room_1} on my left and dive into it.
              ''')
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