define c = Character("")
define friend = Character("Friend")
image bg forest = "forest.jpg"
image bg treehouse = "treehouse.jpg"
image bg insideth = "insideth.jpg"

$ eye = 0
#0 green eye
#1 red eye
$ nose = 0
$ mouth = 0
$ wings = 0
$ body = 0

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
    c "That's probably not the most intelligent observation you've ever made, but it's a start."
    c "Sitting up abruptly, something thin taps you on the face. It's a metal chain."

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
    c "It looks like there's only one exit."
    $ boolean = True
    while boolean:
        menu:
            "Inspect the windows.":
                c "Curious Achievement earned."
                c "You are REALLY high up. Seems like an ordinary treehouse."
            "Lie in bed.":
                c "Sleepy Achievement earned."
                c "The bed's really comfortable. For some reason you were sitting on the floor this whole time."
            "Check the desk.":
                c "There's a single note addressed to you."
                $ boolean = False

    $ player_name = renpy.input("Your name is...")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Lynda"
    c "The letter says: Dear %(player_name)s, I'm scared of you. I'm really scared."

    c "You have woken up in a tree house in the forest."
    menu:
        "What do you want to do?"
        "Jump straight down.":
            c "Gambler Achievement earned."
        "Zipline out of there.":
            c "Adventurer Achievement earned."
        "Stay inside.":
            c "Homebody Achievement earned."

    scene bg forest
    c "You get down and you are in a forest! But now you are starVING."
    menu:
        "How do you get your food?"
        "You are going to hunt a boar, only a boar.":
            c "Meateater Achievement earned."
        "You are going to find some berries or plants or something that cannot eat you.":
            c "Vegetarian Achievement earned."
        "You are going to go fishing and sit for five hours.":
            c "Patient Achievement earned."

    c "There is someone in the distance."
    menu:
        "What do you want to do?"
        "Wave to them and smile in a friendly way.":
            c "Kindness Achievement earned."
        "Call out to them and say hi.":
            c "Sociable Achievement earned."
        "Cry.":
            c "Shy Achievement earned."

    c "Sarah has joined your party."

#work on making it more spooky
#maybe make it mystery

    r "Someone is {i}late{/i}~"
    menu:
        "What should you say to cheer Caspian up?"
        "Shall I record this man in my memory as 'Uptight Ho'?":
            pass
    # This ends the game.

    return
