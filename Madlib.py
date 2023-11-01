




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
    adjective_1 = input("The _____  door opened with a loud creak.")
    adjective_2  = input("The first thing I see is a big _____  body.")
    noun_1 = input(" The wall is covered in _____ .")
    sound_1 = input(" A _____  rang through the halls.")
    sentence_1 = input("As I walk through the halls I get the feeling that _____ .")
    object_1 = input("I spin around and from the dark _____ appears.")
    room_1 = input("I scream and run as fast as I can but it is catching up, I see and _____  on my left and dive into it.")
    onomatopoeia_1 = input("The door makes a loud _____ .")
    object_2 = input(" I crawl under the _____  to hide.")
    adjective_3 = input("I _____  my heart beating in my chest.")
    monster_1 = input(" as he comes around the corner I see two _____  feet come around the corner.")
    verb_1 = input("He _____  around the room and he snarls.")
    verb_2 = input(" He then starts to _____ the air.")
    adjective_4 = input(" All of the sudden there is no _____  and the whole room is completly quite.")
    adverb_1 = input(" Then his eyes go below the bed and he _____ me.")
    print(f'''The {adjective_1} door opened with a loud creak. The first thing I see is a big {adjective_2} body.
        The wall is covered in {noun_1}. A {sound_1} rang through the halls.
        As I walk through the halls I get the feeling that {sentence_1}. I spin around and from the dark {object_1} appears.
        I scream and run as fast as I can but it is catching up, I see and {room_1} on my left and dive into it.
        The door makes a loud {onomatopoeia_1}. I crawl under the {object_2} to hide.
        I {adjective_3} my heart beating in my chest. as he comes around the corner I see two {monster_1} feet come around the corner.
        He {verb_1} around the room and he snarls. He then starts to {verb_2} the air.
        All of the sudden there is no {adjective_4} and the whole room is completly quite.
        Then his eyes go below the bed and he {adverb_1} me. Then everything went dark. ''')
elif level == 3:
    print(f'''  ''')
else:
    level = input;"please choose level through 1-3"








def is_only_letters(letter):
    if letter == " ":
        return False

    for i in letter:
        if i not in "a b c d e f g h i j k l m n o p q r s t u v w x y z".split():
            return False
        return True