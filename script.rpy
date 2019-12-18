#Characters
define c = Character("") #narrator
define p = Character("player_name", dynamic=True)
define player_name = ""
define s = Character("stranger_name", dynamic=True)
define stranger_name = "Strange Boy"

#Background Images
image bg forest = "forest.jpg"
image bg treehouse = "treehouse.jpg"
image bg hunt = "hunt.jpg"
image bg fishd = "fishd.jpg"
image bg foraged = "foraged.jpg"
image bg huntd = "huntd.jpg"
image bg treehoused = "treehoused.jpg"
image bg treehouse_no_note = "treehouse_no_note.jpg"
image bg treehouse_w_note = "treehouse_w_note.jpg"
image bg car = "car.jpg"
image bg driving = "driving.jpg"
image bg house = "house.jpg"
image bg ritual = "ritual.jpg"
image bg alchemy = "alchemy_circle.jpg"
image bg demon_bg = "demon_bg.jpg"
image bush = "bush.jpg"
image zipline = "zipline.jpg"
image ladder = "ladder.jpg"
image white = "#FFF"

#Badges
image adventure2 = "badge_adventure.png"
image art2 = "badge_art.png"
image bystander2 = "badge_bystander.png"
image careful2 = "badge_careful.png"
image curious2 = "badge_curious.png"
image gambler2 = "badge_gambler.png"
image hunt2 = "badge_hunt.png"
image lazy2 = "badge_lazy.png"
image loyal2 = "badge_loyal.png"
image practical2 = "badge_practical.png"
image safety2 = "badge_safety.png"
image savage2 = "badge_savage.png"
image speedy2 = "badge_speedy.png"
image unlucky2 = "badge_unlucky.png"
image veg2 = "badge_veg.png"
image yolo2 = "badge_yolo.png"

#Misc Images
image stranger2 = "stranger_name.png"
image note1 = "note1.png"
image note2 = "note2.png"
image ritual_instructions = "ritual_instructions.png"
image man = "man.png"
image bag_icon = "bag_icon.png"
image inventory = "inventory.png"

#Inventory Items
image berry = "berry.png" #vegetarian
image branch = "branch.png" #gambler #okay
image broken_mirror = "broken_mirror.png" #unlucky
image cell_phone = "cell_phone.png" #yolo
image envelope = "envelope.png"
image fish = "fish.png" #practical
image ladder2 = "ladder.png" #safety
image mask = "mask.png" #bystander
image meat = "meat.png" #hunter
image spray_paint = "spray_paint.png" #eyeforart
image ticket = "ticket.png" #speedy
image whistle = "whistle.png" #loyal
image zip_clip = "zip_clip.png" #adventurer

#Madlibs Variables
define colorz = ""
define scary_object = ""
define death = ""
define scary_place = ""
define audio.ost = "audio/Dreaming.ogg"
define audio2.ost = "audio/posession.mp3"
define audio3.ost = "audio/goth_horror.mp3"
define audio4.ost = "audio/growl.mp3"

define wings = 0
define tail = 0
define eyes = 0
define body = 0
define mouth = 0
#wings
image demon_wings = "demon_wings.png" #jump
image reaper_wings = "reaper_wings.png" #jump
image bat_wings = "bat_wings.png" #zipline
image cute_wings = "cute_wings.png" #safety
#tail
image dragon_tail = "dragon_tail.png" #hunt
image red_tail = "red_tail.png" #hunt
image green_tail = "green_tail.png" #berry
image yellow_tail = "yellow_tail.png" #berry
image blue_tail = "blue_tail.png" #fish
#body
image yellow_body = "yellow_body.png" #speeding
image orange_body = "orange_body.png" #speeding
image blue_body = "blue_body.png" #broken mirror
image green_body = "green_body.png" #broken mirror
image pink_body = "pink_body.png" #graffiti
image purple_body = "purple_body.png" #graffiti
#mouth
image downturned_mouth = "downturned_mouth.png"
image grin_mouth = "grin_mouth.png"
image happy_mouth = "happy_mouth.png"
image stitch_mouth = "stitch_mouth.png"
image straight_mouth = "straight_mouth.png"
#eyes
image black_eyes = "black_eyes.png" #tell him
image x_eyes = "x_eyes.png" #tell him
image blue_eyes = "blue_eyes.png" #secretly
image orange_eyes = "orange_eyes.png" #secretly
image cyclops_eyes = "cyclops_eyes.png" #call out
image slanted_eyes = "slanted_eyes.png" #nothing

label splashscreen:

    scene black
    with Pause(1)

    show text "Jennifer Yu and Abigail Zhong Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "One! In! A Hundred!" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:

    play music audio.ost

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
                $ tail = 3
            "Do nothing.":
                c "Nothing happens. What a surprise."
                $ tail = 4

    scene bg treehouse_w_note

    c "The room lights up."
    c "It's the inside of a treehouse."

    $ curious = False
    $ lazy = False
    $ savage = False

    $ boolean = True
    while boolean:
        menu:
            "Inspect the windows.":
                show curious2 at top
                c "{i}Curious Achievement earned.{/i}"
                hide curious2
                $ curious = True
                c "You're REALLY high up. Seems like an ordinary treehouse."
            "Lie in bed.":
                show lazy2 at top
                c "{i}Lazy Achievement earned.{/i}"
                hide lazy2
                $ lazy = True
                c "The bed's really comfortable. For some reason you were sitting on the floor this whole time."
            "Check the desk.":
                c "There's a single note addressed to you."
                $ boolean = False

    $ player_name = renpy.input("Your name is...")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Lynda"

    scene bg treehouse_no_note
    show note1
    c "{i}To %(player_name)s...{/i}"
    c "You read it and your heart starts pounding faster."
    hide note1

    c "Someone grabs the letter from your hand and you jolt, startled."
    #screen shakes
    show stranger2 at right
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
                show savage2 at top
                c "{i}Savage Achievement earned.{/i}"
                hide savage2
                c "He looks surprised for a moment as if unsure about something but laughs it off."
                s "That's not very nice. Plus, you're the one that called me here."
                $ savage = True

    s "You don't remember my name?"
    $ stranger_name = renpy.input("For some reason, the name at the top of your head is the one that scares you the most.")
    $ stranger_name = stranger_name.strip()
    if stranger_name == "":
        $ stranger_name="Barry"

    p "Oh, you're %(stranger_name)s."
    c "He stares at you for a moment before smiling again."

    s "Yeah, that's me."
    c "You notice him crumple up the note and shove it in his pocket."
    s "Let's get some food. Come over here."
    c "Something feels off about him, but you nod anyway."

    show bag_icon at topleft
    s "Take this bag, you can use it to store all of your items."
    p "Um, sure."

    scene bg treehoused
    show bag_icon at topleft
    s "You can pretty much leave however you want to, which do you prefer?"

    $ gambler = False
    $ okay = False
    $ adventurer = False
    $ safety = False

    menu:
        "Jump straight down. He did say however I want, after all.":
            show gambler2 at top
            c "{i}Gambler Achievement earned.{/i}"
            hide gambler2
            $ gambler = True
            $ wings = 0
            s "Interesting choice... okay."
            scene bush
            show bag_icon at topleft
            p "OUCH! OOF!"
            s "ACK!"
            c "A bush breaks your fall and a piece snaps off."
            show branch:
                xpos 580 ypos 10
            c "{i}Item obtained. Bushy branch.{/i}"
            hide branch
        "...":
            $ wings = 3
            c "You take too long to decide and you suddenly feel a push on your shoulder."
            scene bush
            show bag_icon at topleft
            p "OUCH! OOF!"
            s "ACK!"
            c "A bush breaks your fall and a piece snaps off."
            show branch:
                xpos 580 ypos 10
            c "{i}Item obtained. Bushy branch.{/i}"
            hide branch
            c "Did he just push you?"
            c "...Nah, it couldn't be."
        "Zipline out of there.":
            show adventure2 at top
            c "{i}Adventurer Achievement earned.{/i}"
            hide adventure2
            $ adventurer = True
            $ wings = 1
            s "That hasn't been used in ages, but sure."
            scene zipline
            show bag_icon at topleft
            s "You clip yourself and make it about halfway across when suddenly the rope snap."
            p "OUCH! OOF!"
            s "ACK!"
            show zip_clip:
                xpos 610 ypos 140
            c "{i}Item obtained. Zipline clip.{/i}"
            hide zip_clip
        "Take the ladder.":
            show safety2 at top
            c "{i}Safety First Achievement earned.{/i}"
            hide safety2
            $ safety = True
            $ wings = 2
            s "There are a few steps missing on it, but eh, it'll be fine."
            scene ladder
            show bag_icon at topleft
            s "You make it about halfway down and then suddenly a rung of the ladder snaps off."
            p "OUCH! OOF!"
            s "ACK!"
            show ladder2:
                xpos 580 ypos 10
            c "{i}Item obtained. Ladder piece.{/i}"
            hide ladder2

    scene bg forest
    show bag_icon at topleft

    show stranger2 at right
    c "You both almost die, but make it down somehow."
    c "You look over to %(stranger_name)s to sigh in relief, but then you notice something odd."

    $ scary_object = renpy.input("You get chills. There's something in his pocket. It's a...")
    $ scary_object = scary_object.strip()
    if scary_object == "":
        $ scary_object="taser"

    c "A [scary_object]..."
    s "Phew, we made it down."
    c "He turns to you and you act like you didn't see anything."
    p "Oh yeah... Haha."

    s "Well we have a lot of options, what are you in the mood for?"

    $ hunter = False
    $ vegetarian = False
    $ practical = False

    menu:
        "Something with four legs, like a deer. Maybe watching %(stranger_name)s hunt will reveal something.":
            show hunt2 at top
            c "{i}Hunter Achievement earned.{/i}"
            hide hunt2
            $ hunter = True
            $ tail = 0
        "Something that cannot eat you. Berries or plants seem like a safe option.":
            show veg2 at top
            c "{i}Vegetarian Achievement earned.{/i}"
            hide veg2
            $ vegetarian = True
            if tail != 3 and tail != 4:
                $ tail = 1
        "Something like fish. It'll take a while but at least you can drink some water while you wait.":
            show practical2 at top
            c "{i}Practical Achievement earned.{/i}"
            hide practical2
            $ practical = True
            if tail != 3 and tail != 4:
                $ tail = 2

    if hunter:
        scene bg huntd
        show bag_icon at topleft
        s "Our hunting gear and materials are stored down here. I'll just go grab and get everything set up."
        c "The hunting grounds are beautiful, but somewhat eerie."
        c "You've never hunted before, but %(stranger_name)s seems to be an expert."
        s "Here, give it a try."
        show meat:
            xpos 550 ypos 150
        c "{i}Item obtained. Deer meat.{/i}"
        hide meat
    if vegetarian:
        scene bg foraged
        show bag_icon at topleft
        s "Our gathering gear and materials are stored down here. I'll just go grab and get everything set up."
        c "The forest is beautiful, but somewhat eerie."
        c "You've never gathered food before, but %(stranger_name)s seems to be an expert."
        s "Here, give it a try."
        show berry:
            xpos 520 ypos 10
        c "{i}Item obtained. Wild berries.{/i}"
        hide berry
    if practical:
        scene bg fishd
        show bag_icon at topleft
        s "Our fishing gear and materials are stored down here. I'll just go grab and get everything set up."
        c "The lake is beautiful, but somewhat eerie."
        c "You've never fished before, but %(stranger_name)s seems to be an expert."
        s "Here, give it a try."
        show fish:
            xpos 580 ypos 20
        c "{i}Item obtained. Large fish.{/i}"
        hide fish

    c "You're proud of yourself for accomplishing such a difficult task and turn to the %(stranger_name)s."
    show stranger2 at right
    c "He smiles, but there's something off about it."
    c "You suddenly feel like you did something wrong."
    c "He doesn't leave you to your own thoughts for long."
    s "Let's go back and I'll set up our meal."
    c "After seeing that %(scary_object)s, all of his words just seem a little suspicious."
    c "You keep your expression blank."
    p "Sure."

    hide stranger2

    scene bg forest
    show bag_icon at topleft
    c "A few minutes pass and %(stranger_name)s seems like he won't be done for a while."
    stop music fadeout 1.0
    play music audio2.ost

    #screen shift or shake, noise?
    show man at truecenter
    c "But something in the distance catches your eye. It's a man."
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
            show loyal2 at top
            c "{i}Loyal Achievement earned.{/i}"
            hide loyal2
            $ loyal = True
            $ eyes = 0
            p "Hey %(stranger_name)s, I think there's someone over there."

            show stranger2 at right
            c "%(stranger_name)s's head whips up and he spots the man. His gaze hardens for a moment."
            c "The man visibly freezes and turns to run away."
            hide man
            c "Your heart starts beating faster."
            menu:
                c "You quickly say..."
                "I can go chase him down and see what he wants.":
                    pass
                "I guess he was just having fun by himself over there.":
                    $ eyes = 4

            c "%(stranger_name)s quickly grabs your wrist."
            s "This is a public forest. He could be dangerous, I'll go check on him."
            c "...You want to comment on the irony of that but you shut yourself up."
            c "As %(stranger_name)s walks off, you notice something out of the corner of your eye."
            show whistle:
                xpos 560 ypos 80
            c "{i}Item obtained. Whistle.{/i}"
            hide whistle
        "Tell %(stranger_name)s that you're going to relieve yourself, but secretly go talk to the man.":
            show careful2 at top
            c "{i}Careful Achievement earned.{/i}"
            hide careful2
            $ careful = True
            $ eyes = 1
            p "Hey %(stranger_name)s, I'm going to go to the bathroom real quick."
            s "Okay, don't go too far."
            hide stranger2
            c "He waves you off, unsuspecting."
            hide man
            c "You trudge over to the man, but he drops something and runs off."
            p "Hey, hold on!"
            c "The man doesn't stop running."
            c "You stop to catch your breath, gasping. Crouching down, you pick up another note."
            show note2
            c "You get chills reading it."
            hide note2
            c "There's a mask attached to it."
            show mask:
                xpos 560 ypos -30
            c "{i}Item obtained. Mask.{/i}"
            hide mask
            s "Hey! I'm done over here!"
            c "You shove the note in your pocket and walk back."
            show stranger2 at right
        "Call out to the man.":
            show yolo2 at top
            c "{i}YOLO Achievement earned.{/i}"
            hide yolo2
            $ yolo = True
            $ eyes = 2
            p "HEY! WHAT'S THE MATTER?!"

            show stranger2 at right
            c "%(stranger_name)s's head whips up and he spots the man. His gaze hardens for a moment."
            c "The man visibly freezes and turns to run away."
            hide man
            c "Your heart starts beating faster."
            menu:
                c "You quickly say..."
                "I can go chase him down and see what he wants.":
                    pass
                "I guess he was just having fun by himself over there.":
                    $ eyes = 5

            c "%(stranger_name)s quickly grabs your wrist."
            s "This is a public forest. He could be dangerous, I'll go check on him."
            c "...You want to comment on the irony of that but you shut yourself up."
            c "As %(stranger_name)s walks off, you notice something in the corner of your eye."
            show cell_phone:
                xpos 560 ypos 80
            c "{i}Item obtained. Cell phone.{/i}"
            hide cell_phone
        "Do nothing.":
            show bystander2 at top
            c "{i}Bystander Achievement earned.{/i}"
            hide bystander2
            $ bystander = True
            $ eyes = 3
            show stranger2 at right
            c "%(stranger_name)s's head whips up and he spots the man. His gaze hardens for a moment."
            c "The man visibly freezes and turns to run away."
            hide man
            c "Your heart starts beating faster."
            p "I can go chase him down and see what he wants."

            c "He quickly stops you with a hand around your wrist."
            s "No, it's fine, this is a public forest. He could be dangerous, I'll go check."
            c "...You want to comment on the irony of that but you shut yourself up."
            c "As %(stranger_name)s walks off, you notice something in the corner of your eye."
            show mask:
                xpos 560 ypos 80
            c "{i}Item obtained. Mask.{/i}"
            hide mask

    c "You manage to have a decent meal. Food you obtained yourself tastes better."
    s "This is pretty delicious."
    $ colorz = renpy.input("You find it weird that the color of the food is")
    if colorz == "":
        $ colorz="black"
    s "[colorz] seems pretty normal to me."
    c "You make a face."
    s "Why don't we take a little walk?"

    p "So how exactly did I get up in the treehouse?"
    c "You finally ask. Your memories all seem to be intact up until the forest."
    s "Well, you climbed up yourself obviously."
    p "But why did I sleep here? I have a perfectly good home in Ithaca."
    s "Well we're not in Ithaca right now."
    p "Hm."
    s "%(player_name)s, I have something that might jog your memory."
    p "What is it?"
    s "What was that one place that you never wanted to go to? Was it a church? Or like... a prep school or something?"
    $ scary_place = renpy.input("I think it was...")
    if scary_place == "":
        $ scary_place="college"
    $ scary_place = scary_place.strip()
    s "Yes, [scary_place]! Well you mentioned it to me before we arrived, you had just come from there. Something about it giving you bad memories."
    p "I guess so..."
    s "Well, I'm sure you'll remember eventually."

    scene bg car
    show bag_icon at topleft

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
        c "There's..."
        "...an expensive speeding ticket!":
            show speedy2 at top
            "{i}Speedy Achievement earned.{/i}"
            hide speedy2
            $ speedy = True
        "...a broken mirror!":
            show unlucky2 at top
            "{i}Unlucky Achievement earned.{/i}"
            hide unlucky2
            $ unlucky = True
        "...graffiti all over my car!":
            show art2 at top
            "{i}Eye for Art Achievement earned.{/i}"
            hide art2
            $ eyeforart = True
    p "This is unbelievable!"
    s "I wonder how this happened."
    menu:
        "You probably had something to do with it, you freaky strange boy!":
            $ body = 0
        "What a suspicious thing to say, you're the one that did this, aren't you?!":
            $ body = 1
        "This has your name written all over it, you CLOWN!":
            $ body = 2
        "Hasta la vista! I'm leaving you right now!":
            $ body = 3
        "YOU CRAZYYYYYY BRUH.":
            $ body = 4
        "That's an astute observation. I wonder the same thing.":
            $ body = 5

    c "You quickly realize that you don't actually want to say that..."
    c "You get that out of your mind and take out your bag."
    p "I'm keeping this as evidence!"

    if speedy:
        show ticket:
            xpos 300 ypos 100
        "{i}Item obtained. Speeding ticket.{/i}"
        hide ticket
    if unlucky:
        show broken_mirror:
            xpos 500 ypos 50
        "{i}Item obtained. Broken mirror.{/i}"
        hide broken_mirror
    if eyeforart:
        show spray_paint:
            xpos 900 ypos 150
        "{i}Item obtained. Spray paint bottle.{/i}"
        hide spray_paint

    p "Hey, the keys are in the car. Why don't we take these and look around a bit?"
    c "It's the perfect opportunity for you to find a way out of here."
    s "Sure. I can drive."
    c "You panic immediately and rush to the driver's side."
    p "I don't like people driving my car!"
    c "%(stranger_name)s stares at you."
    s "Okay."

    scene bg driving
    show bag_icon at topleft

    c "You drive for a while. It's mostly trees and more trees and you don't know if you'll have enough gas to make it anywehre."

    s "%(player_name)s, what do you think about life and death?"
    p "What do I think about it?"
    s "What would you consider the scariest way to die? Being eaten by spiders? Suffocation?"
    c "You find the question strange, but it's not like you haven't thought about this before."
    $ death = renpy.input("I would say...")
    if death == "":
        $ death="loneliness"
    s "[death]? That's where I don't agree."
    c "You find the comment a little strange."
    s "Sometimes forms of death exist in life itself."
    p "I don't really get it."
    s "Yeah, that's why I asked."
    c "You still don't get it."

    p "Is that a gate over there?"
    c "%(stranger_name)s is silent for a moment before speaking."
    s "Maybe we shouldn't go out that way."
    c "You know exactly what you want to do now."
    p "Let's just check it out."
    c "You stop the car and open the door. %(stranger_name)s follows you."

    scene bg house
    show bag_icon at topleft

    p "There a mailbox here."
    c "You walk over and open it."
    show envelope:
        xpos 270 ypos -40
    c "{i}Item obtained. Black envelope.{/i}"
    hide envelope
    c "It's a letter addressed... to you?"
    s "Maybe you shouldn't open that."
    p "It's for me so I'm going to open it."
    c "You rip it open and there's an angry message waiting for you."
    p "Hate mail?"
    s "Seems like it."
    p "Wait a second."
    c "It dawns on you all at once."
    p "You said this was a public forest. But this is my property, isn't it?"
    p "My mailbox and my car..."
    c "%(stranger_name)s is silent, his expression unmoving."
    p "Why did you lie?"
    p "Who..."
    p "Who are you?"
    c "%(stranger_name)s steps back and as if on cue, the note from earlier that day falls out of his pocket."
    c "Your heart drops when you read the rest of the note."
    c "{i}And whatever you do, don't trust %(stranger_name)s.{/i}"
    c "You don't know what comes over you, but you run away as fast as you can with one thing on your mind."
    c "The ritual site."
    s "Wait!"
    c "You keep running, %(stranger_name)s hot on your tail."
    c "Somehow, your insticts tell you where to go."

    scene bg ritual
    show bag_icon at topleft
    stop music fadeout 1.0
    play music audio3.ost

    c "When you arrive at the ritual site, %(stranger_name)s has stopped following you. He's nowhere to be found."

    show ritual_instructions
    c "You're drawn to the instructions, as if some force is pulling you and telling you to do this."

    scene bg alchemy
    show bag_icon at topleft
    show inventory:
        xpos 0 ypos 60
    if gambler or okay:
        show branch:
            xpos 53 ypos -180
    if adventurer:
        show zip_clip:
            xpos 53 ypos -180
    if safety:
        show ladder2:
            xpos 53 ypos -180
    if hunter:
        show meat:
            xpos 209 ypos -180
    if vegetarian:
        show berry:
            xpos 209 ypos -180
    if practical:
        show fish:
            xpos 209 ypos -180
    if loyal:
        show whistle:
            xpos 379 ypos -180
    if yolo:
        show cell_phone:
            xpos 379 ypos -180
    if bystander or careful:
        show mask:
            xpos 379 ypos -180
    if speedy:
        show ticket:
            xpos 53 ypos -26
    if unlucky:
        show broken_mirror:
            xpos 53 ypos -26
    if eyeforart:
        show spray_paint:
            xpos 53 ypos -26
    show envelope:
        xpos 209 ypos -26

    image envelope = "envelope.png"

    c "These are the items you collected."

    scene bg alchemy
    show bag_icon at topleft
    show inventory:
        xpos 0 ypos 60
    show bag_icon at topleft

    if gambler or okay:
        show branch:
            xpos 616 ypos -147
    if adventurer:
        show zip_clip:
            xpos 616 ypos -147
    if safety:
        show ladder2:
            xpos 616 ypos -147
    if hunter:
        show meat:
            xpos 1089 ypos -147
    if vegetarian:
        show berry:
            xpos 1089 ypos -147
    if practical:
        show fish:
            xpos 1089 ypos -147
    if loyal:
        show whistle:
            xpos 1028 ypos 97
    if yolo:
        show cell_phone:
            xpos 1028 ypos 97
    if bystander or careful:
        show mask:
            xpos 1028 ypos 97
    if speedy:
        show ticket:
            xpos 679 ypos 97
    if unlucky:
        show broken_mirror:
            xpos 679 ypos 97
    if eyeforart:
        show spray_paint:
            xpos 679 ypos 97
    show envelope:
        xpos 853 ypos -205
    c "All of the items have been placed."
    hide inventory
    s "You finally did it."
    c "You whip your head around and %(stranger_name)s emerges."
    image stranger3 = im.Flip("stranger_name.png", horizontal=True, vertical=False)
    show stranger3 at left
    c "He's holding the note in his hand."
    s "I'm actually the one that wrote this note. Well, all of them."
    s "Don't forget me."

    menu:
        c "A range of emotions go through you, but you ask."
        "So you tricked me?":
            $ mouth = 0
        "You did this all for me?":
            $ mouth = 1
        "Are we friends...?":
            $ mouth = 2
        "What are you planning?":
            $ mouth = 3
        "What was this all for?":
            $ mouth = 4

    s "That's up to you."
    c "Before you can say anything else, %(stranger_name)s steps into the center of the pentacle."
    c "There's a bright flash."
    scene white
    with Pause(1)

    scene black
    with Pause(1)

    show text "A [colorz] haze that runs rampant and follows you like a plague..." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "You feel like you're in an endless maze, trapped in the days in [scary_place]..." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "You're haunted by escaping [death] but your real fears exist in life itself." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "Nobody can see it except for you..." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "Your demon's name is [stranger_name]." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)

    scene bg demon_bg

    if wings == 0:
        show demon_wings
    if wings == 1:
        show bat_wings
    if wings == 2:
        show cute_wings
    if wings == 3:
        show reaper_wings
    if tail == 0:
        show dragon_tail
    if tail == 1:
        show green_tail
    if tail == 2:
        show blue_tail
    if tail == 3:
        show red_tail
    if tail == 4:
        show yellow_tail
    if body == 0:
        show yellow_body
    if body == 1:
        show blue_body
    if body == 2:
        show pink_body
    if body == 3:
        show orange_body
    if body == 4:
        show green_body
    if body == 5:
        show purple_body
    if mouth == 0:
        show downturned_mouth
    if mouth == 1:
        show grin_mouth
    if mouth == 2:
        show happy_mouth
    if mouth == 3:
        show stitch_mouth
    if mouth == 4:
        show straight_mouth
    if eyes == 0:
        show black_eyes
    if eyes == 1:
        show blue_eyes
    if eyes == 2:
        show cyclops_eyes
    if eyes == 3:
        show slanted_eyes
    if eyes == 4:
        show x_eyes
    if eyes == 5:
        show orange_eyes

    play sound audio4.ost
    c "Congratulations on finishing the game!"
    c "{i}Story and Code by Jennifer Yu{/i}"
    c "{i}Graphics by Abigail Zhong{/i}"
    c "{i}Based loosely off of One! Hundred! Demons! by Lynda Barry{/i}"
    c "{i}image resource credits to: https://www.pngfly.com/, https://pngtree.com/, https://www.cleanpng.com/{/i}"
    c "{i}music resource credits to: purple planet : www.purple-planet.com/{/i}"
    c "{i}Thank you for playing!{/i}"

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
