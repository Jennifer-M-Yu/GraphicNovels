define c = Character("")
define p = Character("player_name", dynamic=True)
define player_name = ""
define s = Character("stranger_name", dynamic=True)
define stranger_name = "Strange Boy"
image bg forest = "forest.jpg"
image bg treehouse = "treehouse.jpg"
image bg insideth = "insideth.jpg"
image bg hunt = "hunt.jpg"
image bg fishd = "fishd.jpg"
image bg foraged = "foraged.jpg"
image bg huntd = "huntd.jpg"
image bg treehoused = "treehoused.jpg"

$ eye = 0
$ mouth = 0
$ wings = 0
$ body = 0

label splashscreen:
    scene black
    with Pause(1)

    show text "Jennifer and Abigail Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "Forest of Dreams" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:

    c "..."
    c "....."
    c "........."
    c "It's dark in here."
    c "It's not the best observation you've ever made, but it's a start."
    c "Sitting up abruptly, something cold taps you on the face. It's a thin metal chain."

    $ boolean = True
    while boolean:
        menu:
            "Pull it.":
                $ boolean = False
            "Push it.":
                c "Nothing happens."
            "Do nothing.":
                c "Nothing happens. What a surprise."

    scene bg treehouse

    c "The room lights up."
    c "It's the inside of a treehouse."

    $ curious = False
    $ lazy = False
    $ savage = False

    $ boolean = True
    while boolean:
        menu:
            "Inspect the windows.":
                c "Curious Achievement earned."
                $ curious = True
                c "You're REALLY high up. Seems like an ordinary treehouse."
            "Lie in bed.":
                c "Lazy Achievement earned."
                $ lazy = True
                c "The bed's really comfortable. For some reason you were sitting on the floor this whole time."
            "Check the desk.":
                c "There's a single note addressed to you."
                $ boolean = False

    $ player_name = renpy.input("Your name is...")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Lynda"

    c "The letter says:"
    c "{i}%(player_name)s, I couldn't wake you up so I had to leave you here.{/i}"
    c "{i}But you need to go find the ritual site.{/i}"
    c "{i}Then you need to leave this forest immediately, before he comes.{/i}"
    c "{i}And whatever you do, don't trust--{/i}"

    c "Someone grabs the letter from your hand and you jolt, startled."
    #screen shakes
    c "It's a boy you don't recognize. You didn't even notice him climb into the treehouse."

    s "You're finally awake. I thought you'd never wake up."
    s "We have to leave soon."
    c "You look at the note he's holding in his hand now and wonder if you should bring it up."

    $ boolean = True
    while boolean:
        menu:
            "Ask him to let you finish reading the note.":
                c "He smiles."
                s "Oh, this thing? I'm the one that wrote this, but it's not relevant now."
                c "You're not sure if you fully believe that."
            "Ask him who he is.":
                $ boolean = False
            "Tell him to go away.":
                c "Savage Achievement earned."
                c "He looks surprised for a moment as if unsure about something but laughs it off."
                s "That's not very nice. Plus, you're the one that called me here."
                $ savage = True

    s "You don't remember my name?"
    $ stranger_name = renpy.input("For some reason, the name at the top of your heard is the one that scares you the most.")
    $ stranger_name = stranger_name.strip()
    if stranger_name == "":
        $ stranger_name="Barry"

    p "Oh, you're %(stranger_name)s."
    c "He stares at you for a moment before smiling again."

    s "Yeah, that's me."
    c "You notice him crumple up the note and shove it in his pocket."
    s "Let's get some food. Come over here."

    c "Something feels off about him, but you nod anyway."
    p "Um, sure."

    scene bg treehoused
    s "You can pretty much leave however you want to, which do you prefer?"

    $ gambler = False
    $ adventurer = False
    $ safety = False

    menu:
        "Jump straight down. He did say however I want, after all.":
            c "Gambler Achievement earned."
            $ gambler = True
            s "Interesting choice... okay."
            p "OUCH! OOF!"
            s "ACK!"
            c "A bush breaks your fall and a piece snaps off."
            c "Item obtained. Bushy branch."
        "Zipline out of there.":
            c "Adventurer Achievement earned."
            $ adventurer = True
            s "That hasn't been used in ages, but sure."
            s "You clip yourself and make it about halfway across when suddenly the rope snap."
            p "OUCH! OOF!"
            s "ACK!"
            c "Item obtained. Zipline clip."
        "Take the ladder.":
            c "Safety First Achievement earned."
            $ safety = True
            s "There are a few steps missing on it, but eh, it'll be fine."
            s "You make it about halfway down and then suddenly a rung of the ladder snaps off."
            p "OUCH! OOF!"
            s "ACK!"
            c "Item obtained. Ladder piece."

    scene bg forest
    c "You both almost die, but make it down somehow."
    c "You look over to %(stranger_name)s to sigh in relief, but then you notice something odd."

    $ scary_object = renpy.input("You get chills. There's something in his pocket. It's a...")
    if scary_object == "":
        $ scary_object="taser"

    s "Phew, we made it down."
    c "He turns to you and you act like you didn't see anything."
    p "Oh yeah... Haha."

    s "Well we have a lot of options, what are you in the mood for?"

    $ hunter = False
    $ vegetarian = False
    $ practical = False

    menu:
        "Something with four legs, like a deer. Maybe watching %(stranger_name)s hunt will reveal something.":
            c "Hunter Achievement earned."
            $ hunter = True
        "Something that cannot eat you. Berries or plants seem like a safe option.":
            c "Vegetarian Achievement earned."
            $ vegetarian = True
        "Something like fish. It'll take a while but at least you can drink some water while you wait.":
            c "Practical Achievement earned."
            $ practical = True

    if hunter:
        scene bg huntd
        s "Our hunting gear and materials are stored down here. I'll just go grab and get everything set up."
        c "The hunting grounds are beautiful, but somewhat eerie."
        c "You've never hunted before, but %(stranger_name)s seems to be an expert."
        s "Here, give it a try."
        #tap on screen
        c "Item obtained. Deer meat."
    if vegetarian:
        scene bg foraged
        s "Our gathering gear and materials are stored down here. I'll just go grab and get everything set up."
        c "The forest is beautiful, but somewhat eerie."
        c "You've never gathered food before, but %(stranger_name)s seems to be an expert."
        s "Here, give it a try."
        #tap on screen
        c "Item obtained. Wild berries."
    if practical:
        scene bg fishd
        s "Our fishing gear and materials are stored down here. I'll just go grab and get everything set up."
        c "The lake is beautiful, but somewhat eerie."
        c "You've never fished before, but %(stranger_name)s seems to be an expert."
        s "Here, give it a try."
        #tap on screen
        c "Item obtained. Large fish."

    c "You're proud of yourself for accomplishing such a difficult task and turn to the %(stranger_name)s."
    c "He smiles, but there's something off about it."
    c "You suddenly feel like you did something wrong."
    c "He doesn't leave you to your own thoughts for long."
    s "Wait here and don't go anywhere."
    c "After seeing that %(scary_object)s, his words just seem a little suspicious."
    c "You keep your expression blank."
    p "Sure."
    c "A few minutes pass and %(stranger_name)s seems like he won't be done for a while."

    #screen shift or shake, noise?
    c "Something in the distance catches your eye. It's a man."
    c "%(stranger_name)s is busy so you squint at the figure. The man seems to be trying to contact you."
    c "The man desperately jumps up and down and shakes his head. He makes an X motion with his arms and gestures aggressively."
    c "He points and it takes you a while before you realize he's pointing at %(stranger_name)s."
    c "You raise an eyebrow."

    $ careful = False
    $ loyal = False
    $ yolo = False
    $ bystander = False

    menu:
        "Tell %(stranger_name)s that someone is there.":
            c "Loyal Achievement earned."
            $ loyal = True
            p "Hey %(stranger_name)s, I think there's someone over there."

            c "%(stranger_name)s's head whips up and he spots the man. His gaze hardens for a moment."
            c "The man visibly freezes and turns to run away."
            c "Your heart starts beating faster."
            p "I can go chase him down and see what he wants."

            c "He quickly stops you with a hand around your wrist."
            s "No, it's fine, this is a public forest. He could be dangerous, I'll go check."
            c "...You want to comment on the irony of that but you shut yourself up."
            c "As %(stranger_name)s walks off, you notice something in the corner of your eye."
            c "Item obtained. Whistle."
        "Tell %(stranger_name)s that you're going to relieve yourself, but secretly go talk to the man.":
            c "Careful Achievement earned."
            $ careful = True
            p "Hey %(stranger_name)s, I'm going to go to the bathroom real quick."
            s "Okay, don't go too far."
            c "He waves you off, unsuspecting."
            c "You trudge over to the man, but he drops something and runs off."
            p "Hey, hold on!"
            c "The man doesn't stop running."
            c "You stop to catch your breath, gasping. Crouching down, you pick up another note."
            #insert note
            #That man, he's not of this world.
            #He's one of many who have sought to destroy us.
            #He'll try to earn your favor, but don't trust him.
            s "Hey! I'm done over here!"
            c "You shove the note in your pocket and walk back."
        "Call out to the man.":
            c "YOLO Achievement earned."
            $ yolo = True
            p "HEY! WHAT'S THE MATTER?!"

            c "%(stranger_name)s's head whips up and he spots the man. His gaze hardens for a moment."
            c "The man visibly freezes and turns to run away."
            c "Your heart starts beating faster."
            p "I can go chase him down and see what he wants."

            c "He quickly stops you with a hand around your wrist."
            s "No, it's fine, this is a public forest. He could be dangerous, I'll go check."
            c "...You want to comment on the irony of that but you shut yourself up."
            c "As %(stranger_name)s walks off, you notice something in the corner of your eye."
            c "Item obtained. Cell phone."
        "Do nothing.":
            c "Bystander Achievement earned."
            $ bystander = True
            c "%(stranger_name)s's head whips up and he spots the man. His gaze hardens for a moment."
            c "The man visibly freezes and turns to run away."
            c "Your heart starts beating faster."
            p "I can go chase him down and see what he wants."

            c "He quickly stops you with a hand around your wrist."
            s "No, it's fine, this is a public forest. He could be dangerous, I'll go check."
            c "...You want to comment on the irony of that but you shut yourself up."
            c "As %(stranger_name)s walks off, you notice something in the corner of your eye."
            c "Item obtained. Mask."

    c "You manage to have decent meal. Food you obtained yourself tastes better."
    s "This is pretty delicious."
    $ colorz = renpy.input("You find it weird that the color of the food is")
    if colorz == "":
        $ colorz="black"
    s "Seems pretty normal to me."
    c "You make a face."
    s "Why don't we take a little walk?"

    p "So how exactly did I get up in the treehouse?"
    c "You finally ask. Your memories all seem to be intact up until the forest."
    s "Well, you climbed up yourself obviously."
    p "But why did I sleep here? I have a perfectly good home in Ithaca, NY."
    s "Well we're not in Ithaca right now."
    p "Hm."
    s "%(player_name), I have something that might jog your memory."
    p "What is it?"
    s "What was that one place that you never wanted to go to? Was it a church? Or like... a prep school or something?"
    $ scary_place = renpy.input("I think it was a...")
    if scary_place == "":
        $ scary_place="prep school"
    s "Yes! Well you mentioned it to me before we arrived, you had just come from there. Something about it giving you bad memories."
    p "I guess so..."
    s "Well, I'm sure you'll remember eventually."

    #scene change
    c "You stumble upon an abandoned car."
    p "Isn't this... my car?"
    c "%(stranger_name)s gives you a look and shrugs."
    p "It's kind of run-down but yeah that's definitely my car."
    s "Weird that it's in the middle of the grass like this."
    c "Something on the windshield catches your attention."
    p "Hey!"

    $ speedy = False
    $ unlucky = False
    $ eyeforart = False

    menu:
        c "There's"
        "an expensive speeding ticket!":
            "Speedy Achievement earned."
            $ speedy = True
        "a broken mirror!":
            "Unlucky Achievement earned."
            $ unlucky = True
        "graffiti all over my car!":
            "Eye for Art Achievement earned."
            $ eyeforart = True
    p "This is unbelievable!"
    s "I wonder how this happened."
    p "I'm keeping these as evidence!"

    if speedy:
        "Item obtained. Parking ticket."
    if unlucky:
        "Item obtained. Broken mirror."
    if eyeforart:
        "Item obtained. Spray paint bottle."

    p "Hey, the keys are in the car. Why don't we take these and look around a bit?"
    c "It's the perfect opportunity for you to find a way out of here."
    s "Sure. I can drive."
    c "You panic immediately and rush to the driver's side."
    p "I don't like people driving my car!"
    c "%(stranger_name)s stares at you."
    s "Okay."

    c "It's mostly trees and more trees and you don't know if you'll have enough gas to make it anywehre."

    s "%(player_name), what do you think about life and death?"
    p "What do I think about it?"
    s "What would you consider the scariest way to die? Being eaten by spiders? Suffocation?"
    c "You find the question strange, but it's not like you haven't thought about this before."
    $ death = renpy.input("I would say...")
    if death == "":
        $ death="loneliness"
    s "That's where I don't agree."
    c "You find the comment a little strange."
    s "Sometimes the scariest ways to die are in life itself."
    p "I don't really get it."
    s "Yeah, that's why I asked."
    c "You still don't get it."

    p "Is that a gate over there?"
    c "%(stranger_name)s is silent for a moment before speaking."
    s "Maybe we shouldn't go out that way."
    c "You know exactly what you want to do now."
    p "Let's just check it out."
    c "You stop the car and open the door. %(stranger_name)s follows you."

    p "There a mailbox here."
    c "You walk over and open it."
    c "Item obtained. Black envelope."
    c "It's a letter addressed... to you?"
    s "Maybe you shouldn't open that."
    p "It's for me so I'm going to open it."
    c "You rip it open and there's an angry message waiting for you."
    #insert note
    p "Hate mail?"
    s "Seems like it."
    p "Wait a second."
    c "It dawns on you all at once."
    c "You said this was a public forest. But this is my property, isn't it?"
    c "%(stranger_name)s is silent, his expression unmoving."
    p "Why did you lie?"
    p "Who..."
    p "Who are you?"
    c "%(stranger_name)s steps back and as if on cue, the note from earlier that day falls out of his pocket."
    c "And whatever you do, don't trust %(stranger_name)s."
    c "You don't know what comes over you, but you run away as fast as you can with one thing on your mind."
    c "The ritual site."
    s "Wait!"
    c "You keep running, %(stranger_name)s hot on your tail."
    c "Somehow, your insticts tell you where to go."
    c "You arrive at the ritual site and %(stranger_name)s is nowhere to be found."
    c "A large rock on the ritual site, gives you instructions."
    #insert note
    #place the items of your journey here
    #and this is where it ends
    #but perhaps, something will come of it

    c "All of the items have been placed."
    s "You finally did it."
    c "You whip your head around and %(stranger_name) emerges."
    s "Remember what I told you. Some things are scarier in life than in death."
    c "Before you can say anything, %(stranger_name) steps into the center of the pentacle."
    c "There's a bright flash."

    scene black
    with Pause(1)

    show text "A %(colorz)s haze that runs rampant and follows you like a plague..." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "You feel like you're in an endless maze, trapped in the days inside a %(scary_place)s..." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "You haunted by escaping %(death)s but your real fears are in life..." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "Nobody can see it except for you..." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "Your demon's name is %(stranger_name)s." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "But in the end, a demon is just a demon and if you keep it long enough, it'll be a part of you." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)

    #show demon

    return


    #A [color] [scary thing] that runs rampant and follows you like a plague.
    #You feel like you're in an endless maze as if trapped in [scary place].
    #Nobody can see it except for you.
    #You try to escape [worst way to die], but it haunts you in this form.
    #It's name is [name you chose]
    #But in the end, a demon is just a demon and if you keep it long enough, it'll eventually be harmless."
    #demon is shown

    #plot points
    #stranger acting weird while getting food
    #sees someone in the distance, telling you not to trust stranger
    #finds an abandoned car (which is yours)
    #ends up at a gate with your name on it
    #realizes you're actually just on your own property and not in the middle of nowhere
    #you steal the note from the stranger and run to the ritual site
    #you summon the demon and the stranger ends up being the last piece

    #five items
    #DONE 1. rung of a ladder, clip from the zipline, bush breaks your fall -> you get a branch
    #DONE 2. food: meat, fish, or berries
    #DONE 3. whistle, cell phone, mask
    #DONE 4. after finding an abandoned car (yours), take the keys (there's a little keychain on it)
    #DONE 5. at the gate, takes the hate mail from the mailbox
    #sees note and runs to ritual site

    #DONE color
    #DONE scary thing
    #DONE scary place
    #DONE worst way to die
    #DONE name you chose

    #MADLIBS blurb with shadow of demon
    #Your worst nightmare.
    #A [color] [scary thing] that runs rampant and follows you like a plague.
    #You feel like you're in an endless maze as if trapped in [scary place].
    #Nobody can see it except for you.
    #You try to escape [worst way to die], but it haunts you in this form.
    #It's name is [name you chose]
    #But in the end, a demon is just a demon and if you keep it long enough, it'll eventually be harmless."
    #demon is shown

    # This ends the game.

    return
