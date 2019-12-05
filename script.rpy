define c = Character("")
define p = Character("player_name", dynamic=True)
define player_name = ""
define s = Character("stranger_name", dynamic=True)
define stranger_name = "Strange Man"
image bg forest = "forest.jpg"
image bg treehouse = "treehouse.jpg"
image bg insideth = "insideth.jpg"
image bg hunt = "hunt.jpg"

$ eye = 0
#0 green eye
#1 red eye
$ nose = 0
$ mouth = 0
$ wings = 0
$ body = 0

$ curious = False
$ lazy = False
$ savage = False
$ gambler = False
$ adventurer = False
$ safety = False
$ hunter = False
$ vegetarian = False
$ practical = False
$ hunter = False
$ vegetarian = False
$ practical = False
$ careful = False
$ loyal = False
$ yolo = False

#    scene bg forest
# unsplash.com

#label splashscreen:
#    scene black
#    with Pause(1)
#
#    show text "JenniferIsGod! Presents..." with dissolve
#    with Pause(2)
#
#    hide text with dissolve
#    with Pause(1)
#
#    return

label start:
    #show eileen happy

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
    c "{i}But you need to go find the ritual zone.{/i}"
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
    if stranger_name == "":
        $ stranger_name="Barry"

    p "Oh, you're %(stranger_name)s."
    c "He stares at you for a moment before smiling again."

    s "Yeah, that's me."
    c "You notice him crumple up the note and shove it in his pocket."
    s "Let's get some food. Come over here."

    c "Something feels off about him, but you nod anyway."
    p "Um, sure."

    s "You can pretty much leave however you want to, which do you prefer?"

    menu:
        "Jump straight down. He did say however I want, after all.":
            c "Gambler Achievement earned."
            $ gambler = True
            s "Interesting choice... okay."
        "Zipline out of there.":
            c "Adventurer Achievement earned."
            $ adventurer = True
            s "That hasn't been used in ages, but sure."
        "Take the ladder.":
            c "Safety First Achievement earned."
            $ safety = True
            s "There are a few steps missing on it, but eh, it'll be fine."

    scene bg forest
    c "You both almost die, but make it down somehow."
    c "You look over to %(stranger_name)s to sigh in relief, but then you notice something odd."
    c "There's a red stain on the back of his left leg."

    s "Phew, we made it down."
    c "He turns to you and you act like you didn't see anything."

    s "Well we have a lot of options, what are you in the mood for?"
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

    c "You notice something in the distance. It's a man."
    c "%(stranger_name) is distracted so you squint at the figure. The man seems to desperately be trying to contact you."
    c "The man jumps up and down and shakes his head. He makes an X motion with his arms and gestures aggressively."
    c "He points and you realize he's pointing at %(stranger_name)s."
    c "You raise an eyebrow."

    menu:
        "Tell %(stranger_name)s that someone is there.":
            c "Loyal Achievement earned."
            $ loyal = True
        "Tell %(stranger_name)s that you're going to relieve yourself, but secretly go talk to the man.":
            c "Careful Achievement earned."
            $ careful = True
        "Call out to the man.":
            c "YOLO Achievement earned."
            $ yolo = True

    c "%(stranger_name)s's gaze hardens for a moment."
    s "No, I'll go talk to him."

    #plot points
    #stranger acting weird while getting food
    #sees someone in the distance, telling you not to trust stranger
    #finds an abandoned car (which is yours)
    #ends up at a gate with your name on it
    #realizes you're actually just on your own property and not in the middle of nowhere
    #you steal the note from the stranger and run to the ritual site
    #you summon the demon and the stranger ends up being the last piece

    #five items
    #1. food: meat, fish, or berries
    #2. a flower
    #3. after finding an abandoned car (yours), take the keys (there's a little keychain on it)
    #4. at the gate, takes the hate mail from the mailbox
    #5. the note

    #MADLIBS blurb with shadow of demon
    #Your worst nightmare.
    #A [color] [scary thing] that runs rampant and follows you like a plague.
    #You [embarassing action] on your way to [scary place].
    #Nobody can see it except for you.
    #You try to escape [worst way to die], but it haunts you in this form.
    #But in the end, a demon is just a demon and if you keep it long enough, it'll eventually be harmless."
    #demon is shown

    # This ends the game.

    return