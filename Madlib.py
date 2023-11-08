




name = input("what is your name?")
play = input("Would you like to play yes or no")
while play == "yes":
    level = int(input(
        "Hi " + name + " what level would you like to play? level 1-3?"
))

    if level == 1:
        noun_1 = input("Once upon a time in the great land of _____(noun) ") 
        adjective_1 = input("In this _____(adjective) kingdom,")
        noun_2 = input("there was a great witch whos name was _____(noun)")
        adjective_2 = input("She had a _____(adjective) smile")
        adjective_3 = input("and ____(adjective) hair")
        onomatopoeia_1 = input("One day she was brewing her potions she heard a _____(noise)")
        noun_3 = input("She ran outside and saw one of her cats ____(adjective)")
        object_1 = input("'Curse you' she yeled to the sky and she ran to get her broom and _____(object)")
        monster_1 = input("She was heading towards the _____(type of monster) civilization when suddenly she got knocked out of the sky")
        onomatopoeia_2 = input("She fell towards the ground and heard her bones _____(noise)")
        adjective_4 = input("She limped over behind a tree and felt her heart _____(adjective)")
        noun_4 = input("A snapping of _____(noun) came from the bushes on her left")
        adjective_5 = input("Her eyes dilated in fear and she started breathing harder as the _____(adjective) beast came out of the bushes")
        adjective_6 = input("but it was just a ______(adjective)")
        animal_1 = input(f"but it was just a {adjective_6} _____(animal)")
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
        adjective_1 = input("The _____(adjective)  door opened with a loud creak.")
        adjective_2  = input("The first thing I see is a big _____(adjective)  body.")
        noun_1 = input(" The wall is covered in _____(noun) .")
        sound_1 = input(" A _____ (sound) rang through the halls.")
        sentence_1 = input("As I walk through the halls I get the feeling that _____(multiple words) .")
        object_1 = input("I spin around and from the dark _____ appears.")
        room_1 = input("I scream and run as fast as I can but it is catching up, I see and _____ (room) on my left and dive into it.")
        onomatopoeia_1 = input("The door makes a loud _____(sound) .")
        object_2 = input(" I crawl under the _____(object)  to hide.")
        adjective_3 = input("I _____(adjective)  my heart beating in my chest.")
        monster_1 = input(" as he comes around the corner I see two _____ (monster) feet come around the corner.")
        verb_1 = input("He _____ (verb) around the room and he snarls.")
        verb_2 = input(" He then starts to _____ (verb) the air.")
        adjective_4 = input(" All of the sudden there is no _____ (adjective) and the whole room is completly quite.")
        adjective_5 = input(" Then his eyes go below the bed and he _____ (adjective) me.")
        print(f'''The {adjective_1} door opened with a loud creak. The first thing I see is a big {adjective_2} body.
            The wall is covered in {noun_1}. A {sound_1} rang through the halls.
            As I walk through the halls I get the feeling that {sentence_1}. I spin around and from the dark {object_1} appears.
            I scream and run as fast as I can but it is catching up, I see and {room_1} on my left and dive into it.
            The door makes a loud {onomatopoeia_1}. I crawl under the {object_2} to hide.
            I {adjective_3} my heart beating in my chest. as he comes around the corner I see two {monster_1} feet come around the corner.
            He {verb_1} around the room and he snarls. He then starts to {verb_2} the air.
            All of the sudden there is no {adjective_4} and the whole room is completly quite.
            Then his eyes go below the bed and he {adjective_5} me. Then everything went dark. ''')
    elif level == 3:
        noun_1 = input("I opened up my _____(noun).")
        animal_1 = input("I tred to ook around and realized there was a _____(animal) trap on my head.")
        adjective_1 = input(" The loud speakers started playing and said you have been found _____(adjective).")
        noun_1 = input("You will have one minute to escape other wise it will cut of your _____(noun).")
        adjective_2 = input(" The only way to escape is to _____(adjective) your dog.")
        adjective_3 = input("If you _____(adjective) your dog you will find a key inside his heart.")
        verb_1 = input(" My heart starts _____(verb).")
        adjective_4 = input("My palms are getting _____(adjective).")
        adjective_5 = input(" What do I do? After about 10 seconds I pick up the gun and _____(adjective) him.")
        object_1 = input("Using the _____(object) I cut open a hole in his chest and start digging around.")
        time_1 = input(" Time is ticking down their is only _____(time) left. ")
        object_2 = input(" Finally I found It and I grab the _____(object).")
        noun_2 = input(" I rise up to put the key in the _____(noun).")
        noun_3 = input(" Suddenly I can see my body and everything went _____(noun). ")
        print(f'''I opened up my {noun_1}. I tred to ook around and realized there was a {animal_1} trap on my head.
            The loud speakers started playing and said you have been found {adjective_1}. You will have one minute to escape other wise it will cut of your {noun_2}.
            The only way to escape is to {adjective_2} your dog. If you {adjective_3} your dog you will find a key inside his heart. Your time starts now.
            My heart starts {verb_1}. My palms are getting {adjective_4}. What do I do? After about 10 seconds I pick up the gun and {adjective_5} him.
            Using the {object_1} I cut open a hole in his chest and start digging around. Where is it? Wheres the heart? 
            Time is ticking down their is only {time_1} left. Finally I found It and I grab the {object_2}. I rise up to put the key in the {noun_2}.
            Suddenly I can see my body and everything went {noun_3}. ''')
    else:
        level = input;"please choose level through 1-3"
    play = input("would you like to play again yes or no")







def is_only_letters(letter):
    if letter == " ":
        return False

    for i in letter:
        if i not in "a b c d e f g h i j k l m n o p q r s t u v w x y z".split():
            return False
        return True