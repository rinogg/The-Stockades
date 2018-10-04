import sys, time, random
import winsound

###### THE STOCKADES ######
################################################################################

########### FEATURES ############

# READ ALL NOTES BEFORE PUBLISHING

def print_s(str):
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(.01)
    print ""

def death():
    print """                               ,--.
                              (    }
                              K,   }
                             /  `Y`
                        _   /   /
                       {_'-K.__/
                         `/-.__L._
                         /  ' /`\_}
                        /  ' /
                ____   /  ' /
         ,-'~~~~    ~~/  ' /_
       ,'             ``~~~%',
      (                     %$  Y
     {                      %$  I
    {      -                 %  `.
    |       ',                %  )
    |        |   ,..__      __. Y
    |    .,_./  Y ' / ^Y   J   )|
    \           |' /   |   |   ||
     \          L_/    . _ (_,.'(
      \,   ,      ^^""' / |      )
        \_  \          /,L]     /
          '-_`-,       ` `   ./`
             `-(_            )
                 ^^\..___,.--` """
    winsound.PlaySound('death.wav', winsound.SND_FILENAME)
    print_s("\n              ##### YOU DIED #####")
    raw_input("                   Press Enter to play again.\n")
    #always include Start function here#
    #make sure loop is correct and resets vars

    start()

def stats():
        print "\n               STATS:"
        print "------------------------------------------------"
        print "You have %d HP" % hp
        #there was global fire on this line
        #check need for global on vars
        if torch:
            print "You are using a torch to light the rooms."
        if silverkey:
            print "You have a silver key."
        if goldenkey:
            print "You have a golden key."
        if knife:
            print "You have a knife."
        if sword:
            print "You have a sword."
        if armour:
            print "You are wearing a chestplate as armour."
        if fire_ward:
            print "You have been warded against fire magic."
        if frost_ward:
            print "You have been warded against frost magic."
        if potion:
            print "You have a drinkable health potion."
        print "------------------------------------------------\n"

def music():
    for i in range(2):
        winsound.PlaySound("mus.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        #make sure you have mus.wav file in the same folder as .py    # REMEMBER TO EDIT MUSIC FOR LENGTH

def start_vars():
    #include this function in the first room
    global hp
    global silverkey
    global goldenkey
    global knife
    global sword
    global armour
    global potion
    global fire_ward
    global frost_ward
    global torch
    global goblin1
    global hench1
    global goblin2
    global frost_lich
    global fire_lich
    global name
    #hp
    hp = 100

    #items
    silverkey = False
    goldenkey = False
    knife = False
    sword = False
    armour = False
    potion = False
    fire_ward = False
    frost_ward = False
    torch = False

    #enemies
    goblin1 = True
    hench1 = True
    goblin2 = True
    frost_lich = True
    fire_lich = True

    #name
    name = ""

def damage(truedmg):

    global hp
    global knife
    global sword
    global armour
    global potion
    global fire_ward
    global frost_ward




    if armour and truedmg <= 15:
        truedmg = 0
    elif sword and truedmg <= 10:
        truedmg = 0
    elif knife and truedmg <= 5:
        truedmg = 0
    elif armour and truedmg > 15:
        truedmg -= 15
    elif sword and truedmg > 10:
        truedmg -= 10
    elif knife and truedmg > 5:
        truedmg -= 5

    hp -= truedmg

    print "    \n#### YOU RECEIVE %d DAMAGE ####\n" % truedmg
    time.sleep(1)

    if hp <= 0:
        death()

def potion_drink():
    global potion
    global hp

    print_s("You search your bag.")
    time.sleep(1)

    if potion:
        print "You drink your health potion and gain 35 HP!\n"
        hp += 35
        potion = False

    elif not potion:
        print "You don't have any potions.\n"

def greasy_spider():

    print_s("A greasy spider crawls out of a hole. It skitters towards you and bites your leg. You start stabbing it desperately.")
    print_s("The fight is shorter than you thought it would be.")
    print_s(". . .")
    time.sleep(3)
    damage(18)
    print "\nYou kill the spider.\n"
    time.sleep(1)
    print_s("The spider is dead on the floor. His body is in pieces and oozing yellow grease. Eww. There is a door at the north and one at the south, where you first came in. What do you do?")

def ogre():

    print_s("An ogre comes charging through the door as you step in. The ogre is angry. He jumps at you and you start fighting.")
    print_s("The fight takes a few minutes. Your slim body aids you in jumping all over the room dodging the ogre's charges. He still manages to hit you.")
    print_s(". . .")
    time.sleep(3)
    damage(28)
    print "\nYou kill the ogre.\n"
    time.sleep(1)
    print_s("The ogre is dead on the floor. He was naked and fat. No items on him. There is a door at the north and one at the south, where you first came in. What do you do?")

def rogue():

    print_s("Suddenly a stealthy rogue appears from the shadows. He is here, just as you are, to claim the gold reward. He thinks you are one of the stockades prisoners and attacks you.")
    print_s("You catch the rogue in mid-air and you cut his throat. He still managed to stab you though.")
    print_s(". . .")
    time.sleep(3)
    damage(23)
    print "\nYou kill the rogue.\n"
    time.sleep(1)
    print_s("The rogue is dead on the floor. No interesting loot on his body. There is a door at the north and one at the south, where you first came in. What do you do?")

def clear_room():
    time.sleep(1)
    print_s("It was probably just the wind...")
    print_s("The room is empty. There is a door at the north and one at the south, where you first came in. What do you do?")

def randenc():

    enemies = [greasy_spider, ogre, rogue]
    chance = [clear_room, enemies]
    try:
        random.choice(random.choice(chance))()
    except TypeError:
        clear_room()

def puzzle():

    global goldenkey

    print_s("You approach the small iron box and take it in your hands. It says on it \"Open the box for the golden key\". The box has two wheels to turn for you to enter a number.")
    print_s("The imprint on the box is a grid of numbers:")
    print "\n--------------"
    print "| 1 + 4 = 12  |"
    print "| 2 + 9 = 24  |"
    print "| 3 + 14 = 36 |"
    print "| 5 + 24 = ?? |"
    print "--------------"
    print "\nWhat number do you enter? Type 'leave' to leave the box."

    while True:

        action = raw_input("\n> ")

        if action == "stats":
            stats()
            continue

        if action == "60":
            print_s("The box shatters to pieces instantly and a beautiful golden key drops on the floor. You bend and pick it up.")
            goldenkey = True
            print_s("\nYou now have the golden key!\n")
            keyroom()

        elif action == "leave":
            print_s("You give up and put the box down. Maybe another time?")
            keyroom()

        else:
            print "Invalid. Try again."


########### FEATURES ###########

################################################################################

########### ROOMS ############

def start():

    global name

    music()
    start_vars()
    print "Loading..."
    print_s("\n#################################################################")
    print "-type \'stats\' anytime to see your items and health"
    print "-picking up items will increase your combat efficiency"
    print "-do not use capital letters for commands"
    print "-do not press ENTER unless prompted (you will take damage)"
    print_s("#################################################################")
    time.sleep(4)
    print "\n"
    print "\n~~~You enter the gate and you see the wizard sitting down at a desk smoking his pipe."
    print "He says: Ah. Another brave soldier coming to aid. Welcome to the Stockades."
    print "This prison acts as a reformatory for the unruly denizens of our city and many...other beings."
    print "However, every 5 years we organise a purge to cleanse our holdings from those who failed to be...erhm...reformed."
    print "During the purge period, we invite heroes and champions from across our realm to climb down in the prison and slay everything in there."
    print "I hope you realise that the amount of gold we'll pay you is also based on the very high risk that you will die."
    print "All you have to do in order to get started is take a seat and sign this contract here.\n....."
    print "You sit down and the wizard hands you a piece of paper. You can't understand any of the terms as the writing is indesciphrable. You see a field underneath everything saying:"
    name = raw_input("\nSign with your name here: ") # name tre sa fie global

    print_s("\n\"Very well, %s\"" % name)
    print_s("The wizard then stands up and pulls a lever, a trap door opens under you and you fall into a dark pit along with the chair you were sitting on.")
    print_s("....")
    time.sleep(2)
    print_s("You hit the floor hard and the chair turns to splinters under you.")
    print_s("You stand up, aching from the fall, and shake your head trying to regain your wit.")
    torch_room()

def torch_room():

    global torch

    while True:

        if not torch: #daca n-ai torta
            print_s("\n~~~You are now in a dark room with walls of rough stone. One of the walls is lit by a torch. You cannot see very well and could use some light. What do you do?")

            while True:

                action = raw_input("> ")

                if action == "stats":
                    stats()
                    continue #mersi ovidiu!!

                if "torch" in action:
                    print_s("\nYou grabbed the torch and can see what is in the room.")
                    time.sleep(1)
                    torch = True
                    break
                    #return torch
                    #fara return nu merge? de ce?

                else:
                    print "Invalid. Try again."

                continue #tine minte asta - continue te scoate din cel mai apropiat loop

        else: #daca ai torta
            print_s("\n~~~Aside from two cell doors on the left and right and one wooden door in the middle to the north, this room is empty. The floor is muddy and scattered with splinters from the broken chair. You can hear faint screams through the walls.")
            print_s("Which door do you take?")

            while True:

                action = raw_input("> ")

                if action == "stats":
                    stats()
                    continue

                if "left" in action or "right" in action or "cell" in action:
                    print_s("You approach one of the cell doors slowly. The door is locked. You can make out the shape of a few skulls inside. Nothing of interest here.")
                    continue

                elif "middle" in action or "center" in action or "wooden" in action or "north" in action:
                    print_s("The door creaks open. You step into the next chamber.")
                    goblin1_room()

                else:
                    print "Invalid. Try again."

def goblin1_room():

    global goblin1
    global knife

    if goblin1: # DACA E VIU GOBLINU
        print_s("\n~~~You pace slowly as you start to make out the shape of a goblin munching on a piece of mutton in the corner of the room. You can see a door right in front of you.")
        print_s("You are afraid to approach the door with the goblin in the room.")
        print_s("To your immediate left there is a wooden table stained with dried wine. On the table you see a dim candle, an empty piece of parchment and a knife.")
        print_s("The goblin sees you.")
        print_s("What do you do?")

        while True:

            global knife

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "knife" in action and not knife:
                knife = True
                print_s("You quickly grab the knife from the table. The goblin starts growling and shrieking. What do you do?")
                continue

            if "knife" in action and knife:
                print_s("You already have the knife. The goblin prepares to attack you. What do you do?")
                continue

            if "kill" in action or "attack" in action or "fight" in action:
                print_s("You jump at the goblin's throat. Punches and stabs. Slashes and screams.")
                print_s(". . .")
                time.sleep(2)
                damage(8)
                print_s("\nYou kill the goblin.")
                goblin1 = False
                goblin1_room()

            else:
                print_s("The goblin notices you are distracted and slashes you with his claws. What do you do?!")
                damage(11)


    if not goblin1: # DACA E MORT GOBLINU

        if not knife:
            print_s("\n~~~A knife is on the table. The room is now quiet with the goblin's carcass still warm on the floor.")
            print_s("There are doors at the north and south of the room. The northern door appears to be of heavy steel and is slightly ajar.")
            print_s("What do you do?")

            while True:

                action = raw_input("\n> ")

                if action == "stats":
                    stats()
                    continue

                if "potion" in action:
                    potion_drink()
                    continue

                if "north" in action or "northern" in action or "steel" in action or "heavy" in action:
                    print_s("You step into the next chamber.")
                    prophecy_room()

                if "south" in action or "southern" in action or "wooden" in action:
                    print_s("You step into the room where you first fell.")
                    torch_room()

                if "knife" in action:
                    knife = True
                    print_s("You take the knife from the table and shove it under your belt. What do you do next?")
                    continue

                else:
                    print "Invalid. Try again."

        elif knife:
            print_s("\n~~~The room is now quiet with the goblin's carcass still warm on the floor.")
            print_s("There are doors at the north and south of the room. The northern door appears to be of heavy steel and is slightly ajar.")
            print_s("What do you do?")

            while True:

                action = raw_input("\n> ")

                if action == "stats":
                    stats()
                    continue

                if "north" in action or "steel" in action or "heavy" in action:
                    print_s("You step into the next chamber.")
                    prophecy_room()

                if "south" in action or "wooden" in action:
                    print_s("You step into the room where you first fell.")
                    torch_room()

                else:
                    print "Invalid. Try again."

        else:
            print "Invalid. Try again."






        #poti lua cutitu daca NU e luat
        #daca e luat - atunci e gol

    #daca goblinu e viu

        # poti lua cutitu SAU/SI poti omora goblinu
            # daca ai cutitu iei dmg mai mic
            # daca n-ai cutitu iei dmg mai mare

    # daca goblinu e mort
        #poti lua cutitu daca nu e luat
        #daca e luat - empty room

    # te poti intoarce si inapoi in torch_room

def prophecy_room():

    print_s("\n~~~This room is larger than the others. You see wooden doors with steel bars to the north, south, west and east. You also see a large readable plaque on the floor. The eastern door has a silver lock on it. The western door has \"TREASURE\" written on it with blood. \nWhat do you do?")

    while True:

        action = raw_input("\n> ")

        if action == "stats":
            stats()
            continue

        if "potion" in action:
            potion_drink()
            continue

        if "inscription" in action or "read" in action or "plaque" in action:
            print_s("You kneel and get a closer look. The inscription reads in capital letters:")
            print_s("*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*")
            print_s(""" BEWARE FOOLS, FOR ON THE 501st PURGE OF THE STOCKADES, \nTHE WRATH OF THE SOULS TORTURED HERE SHALL COALESCE INTO UNSPEAKABLE HORRORS. \nMANY WILL TRY, MANY WILL FAIL. ONLY THOSE ACQUAINTED BY FIRE AND ICE SHALL PREVAIL. """)
            print_s("*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*")
            time.sleep(3)
            print_s("\nYou stand back up. Chills run down your spine as you remember this actually is the 501st purge.\n")
            time.sleep(3)
            print_s("You regain your courage. Which door do you try?")
            continue

        elif "north" in action or "northern" in action or "wooden" in action or "wooden" in action:
            print_s("The northern door opens at the lightest touch. You step in the room.")
            hench1_room()

        elif "west" in action or "western" in action or "treasure" in action:
            print_s("You push the door that says \"TREASURE\" and step in the room.")
            goblin2_room()

        elif "east" in action or "eastern" in action or "lock" in action or "silver" in action:

            if silverkey and frost_ward:
                print_s("Since you have been warded against frost, the door of this room has frozen into a block of ice. It is impossible to open.")
                print_s("What do you do?")
                continue

            if not silverkey:
                print_s("The door has a large silver lock. You need a key to open this door.")
                continue

            elif silverkey:
                print_s("You pull the key out of your pouch and excitedly turn the lock open. The chains fall from the door but the lock magically remains in place. However, the door opens with a loud crack.")
                time.sleep(1)
                frost_ward_room()


        elif "south" in action or "southern" in action:
            print_s ("You go back in the room where you killed the goblin.")
            goblin1_room()

        else:
            print "Invalid. Try again."
    #inscription

    #NORTH HENCHMEN + KEY drop

    #EAST YOU NEED key

    #WEST YOU GET SWORD


    #aici sunt 4 usi si 1 placa de citit

def goblin2_room():
    global goblin2
    global sword

    if goblin2: #DACA GOBLINU E IN VIATA
        print_s("\n~~~This room is faintly lit by torches. There is a goblin here pacing back and forth. The goblin is no match for you, but this one is armed with a longsword. Behind the goblin you can see a treasure chest. You are pondering your odds. What do you do?")

        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            elif "attack" in action or "kill" in action or "fight" in action or "stab" in action:
                print_s("You charge head-on at the goblin. Punches and stabs. Slashes and screams.")
                print_s(". . .")
                time.sleep(2)
                damage(13)
                print_s("\nYou kill the goblin.")
                goblin2 = False
                time.sleep(1)
                print_s("You approach the treasure chest...but sadly, notice it's only filled with cobweb.")
                print_s("You mutter in anger but realise the goblin had a beautiful sword. You pick it up and sheathe it on your back.")
                time.sleep(1)
                print_s("\nYou now have a sword!\n")
                time.sleep(1)
                sword = True
                goblin2_room()

            else:
                print_s("The goblin takes advantage of having a superior weapon and attacks you. You did not riposte in time and got hurt. You cannot run. What do you do?!")
                damage(13)

    elif not goblin2:
        print_s("\n~~~The goblin is just as you left him. Gutted on the floor. The treasure chest is empty. Nothing of interest here aside from the door which you came through. What do you do?")

        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "door" in action or "back" in action or "return" in action or "leave" in action:
                print_s("You open the door and slam it behind you.")
                prophecy_room()

            else:
                print "Invalid. Try again."

def hench1_room():

    global hench1
    global silverkey

    if hench1:
        print_s("\n~~~You step into the room with confidence only to spot a bald, fat thug facing away from you. You immediately notice a large silver key dangling at his belt.")
        print_s("There are doors at the north and south, from where you first arrived. You would need to kill the thug first. What do you do?")

        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "potion" in action:
                potion_drink()
                continue

            elif "attack" in action or "kill" in action or "fight" in action or "stab" in action:
                print_s("You tactically attack the thug. Several blows occur. You fight well but are hurt.")
                print_s(". . .")
                time.sleep(2)
                damage(23)
                print_s("\nYou kill the thug.")
                hench1 = False
                time.sleep(1)
                print_s("You bend over the thug's dead body. A stench of garlic makes you gag. You pick up the key and quickly stand up.")

                time.sleep(1)
                print_s("\nYou now have the silver key! You think what wonders it may unlock.\n")
                time.sleep(1)
                silverkey = True
                hench1_room()

            else:
                print_s("The thug uses his broad fists to double punch you right in the face. You fail to riposte. What do you do?!")
                damage(18)


    elif not hench1:
        print_s("\n~~~The room absolutely reeks of garlic. You wonder how someone can smell of garlic so bad as you step over the thug's dead body. There are doors at the north and south, from where you first arrived. The northern door appears to have frost all around it and you hear a dangerous hum from it.")
        print_s("What do you do?")
        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "potion" in action:
                potion_drink()
                continue

            if "south" in action or "southern" in action:
                print_s("You step into the room with the prophecy inscription.")
                prophecy_room()

            elif "north" in action or "northern" in action or "frozen" in action:
                print_s("You approach the frozen door. You get very cold but still push it. You notice it doesn't open easily so you kick it open. You step into a large chamber.")
                time.sleep(1)
                frost_lich_room()

            else:
                print "Invalid. Try again."

def frost_ward_room():

    global frost_ward

    print_s("\n~~~You are in awe of the blue magic floating around in this room. It's cold but somehow you don't feel it. In the middle, on a pedestal a magical scroll is floating. There is writing on the pedestal saying \"Those who touch it will be offered protection against frost magic\"")
    time.sleep(3)
    print_s(". . .")
    print_s("You touch the scroll but your feet freeze completely and you cannot move. The frost is slowly moving up your body.")
    time.sleep(2)
    print_s("You observe runes on the scroll start forming into numbers.")
    print_s("Solve the puzzle to survive.\n")
    print_s("========================================================")
    print_s("23 8 1 20 . 9 19 . 20 8 5 . 8 9 7 8 5 19 20 . ")
    print_s("13 15 21 14 20 1 9 14 . 9 14 . 20 8 5 . 23 15 18 12 4 ?")
    print_s("========================================================\n")
    print_s("What is the answer to this riddle?")

    while True:

        action = raw_input("\n> ")

        if action == "stats":
            stats()
            continue

        if "potion" in action:
            potion_drink()
            continue

        if "everest" in action or "Everest" in action:

            time.sleep(1)
            print_s("You shout in pain: EVEREST!. The icy shackles holding you in place suddenly break and you feel a warmth filling you.")
            time.sleep(2)
            print_s("You are warded against all frost magic!")
            time.sleep(1)
            frost_ward = True
            print_s("You faint and after a few minutes wake up outside of the room.")
            time.sleep(2)
            prophecy_room()

        else:
            print_s("The frost climbs up on your body even higher. It hurts. You must solve this puzzle quickly!")
            damage(15)

def frost_lich_room():

    global frost_ward
    global frost_lich


    if frost_lich:
        print_s("\n~~~This room is large and quite tall. You feel the blood freezing in your veins as you look up. Above you floats a powerful being radiating with blue light.")
        time.sleep(2.5)
        print_s("It is wearing a beautiful black robe embroidered with blue markings. A skull for a head with blue fire seeping from its mouth and eyes. It is the much feared frost lich in all its might.")
        time.sleep(2.5)
        print_s("The frost lich turns at you and freezes all the doors of the room. You cannot escape.")
        print_s("The lich says in a slithering, echoing voice:")
        time.sleep(1)
        print_s("\"Ah! Another challenger. Let's see if you are worthy, %s!\"" % name)
        print_s("What do you do?")

        while True:

            action = raw_input("\n> ")
            condition = "attack" in action or "kill" in action or "fight" in action or "stab" in action or "destroy" in action or "frost" in action or "ward" in action

            if action == "stats":
                stats()
                continue

            if frost_ward and condition:
                print_s("You can feel your arms from shoulder to fist, swelling with a visible blue energy. You feel powerful.")
                time.sleep(1)
                print_s("You and the lich fight almost as equals. Your attacks rip through the lich's essence damaging him tremendously.")
                print_s(". . .")
                time.sleep(2)
                print_s("The lich's attacks are powerful and you are hurt.")
                print_s(". . .")
                time.sleep(2)
                damage(23)
                print_s("\nYou destroy the frost lich.\n")
                frost_lich = False
                time.sleep(1)
                print_s("The lich appears to vanish from existence. Its skull hits the ground and cracks. The ice on the doors melts completely.")
                frost_lich_room()
                time.sleep(1)

            elif not frost_ward and condition:
                print_s("You try to hit the lich but your attacks pass right through him.")
                print_s("The lich laughs at you: \"PAH! You fool. You have no protection. You shall DIE!\"")
                print_s(". . .")
                time.sleep(2)
                damage(130)

            else:
                print "The lich instantly hurls an icicle that pierces your chest. It hurts badly."
                time.sleep(1)
                damage(35)


    elif not frost_lich:

        print_s("\n~~~A large room formerly inhabited by the frost lich. There are doors to north, south, west and east.")
        print_s("The northern door says \"BEWARE\".")
        print_s("There is a smell of garlic seeping from under the southern door.")
        print_s("The eastern door has a golden lock on it.")
        print_s("The western door is plain and made out of wood.")
        print_s("What do you do?")

        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "potion" in action:
                potion_drink()
                continue

            if "east" in action or "eastern" in action or "lock" in action or "golden" in action or "gold" in action:

                if not goldenkey:
                    print_s("The door has a large golden lock. You need a key to open this door.")
                    continue

                elif goldenkey:
                    print_s("You pull the key out of your pouch and excitedly turn the lock open. The golden lock clicks and clacks and opens. You step into the room.")
                    time.sleep(1)
                    armour_room()

            elif "north" in action or "northern" in action:
                print_s("You step into the next chamber.")
                encounter_room1()

            elif "south" in action or "southern" in action or "garlic" in action:
                print_s("You gag from the smell of garlic.")
                hench1_room()

            elif "west" in action or "western" in action or "plain" in action or "wood" in action or "wooden" in action:
                print_s("You turn the handle of the wooden door and it opens.")
                keyroom()

            else:
                print "Invalid. Try again."

def keyroom():

    global goldenkey

    if not goldenkey:

        print_s("\n~~~The room has no other doors, windows or anything special. There is only a square shaped iron box on the floor. You look at the box and realise it's a number riddle.")
        print_s("Do you try to solve it?")

        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "Yes" in action or "yes" in action or "puzzle" in action or "box" in action:
                puzzle()

            elif "no" in action or "No" in action or "leave" in action or "back" in action:
                print_s("You don't feel smart today. You leave the room.")
                frost_lich_room()

            else:
                print "Invalid. Try again."

    if goldenkey:

        print_s("\n~~~There are only small iron shards on the floor. The room is empty. You have the golden key. What do you do?")

        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "potion" in action:
                potion_drink()
                continue

            if "door" in action or "back" in action or "return" in action or "leave" in action:
                print_s("You open the door and slam it behind you.")
                frost_lich_room()

            else:
                print "Invalid. Try again."

def armour_room():

    global armour
    global potion

    if armour:
        print_s("\n~~~The room is beautiful and looks comfortable. You are happy with what you found in the chest. You can only turn back. What do you do?")

        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "potion" in action:
                potion_drink()
                continue

            if "treasure" in action or "chest" in action:
                print_s("You have already emptied the contents of the chest.")
                continue

            if "back" in action or "leave" in action or "return" in action or "run" in action:
                print_s("You step out of the room.")
                frost_lich_room()

            else:
                print "Invalid. Try again."

    elif not armour:

        print_s("\n~~~You step into this room and feel calm. It is very clean and beautiful. Well-lit and decorated with all sorts of paintings. There is also a comfortable cushioned chair and a table. On the table there is a treasure chest.")
        print_s("What do you do?")


        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "open" in action or "treasure" in action or "take" in action or "chest" in action:
                print_s("The treasure chest opens easily. Inside there is a engraved chestplate and a red health potion. You take the potion and you put the chestplate on you. It fits as if made for you.")
                time.sleep(2)
                print_s("\nYou now have a drinkable health potion!\n")
                time.sleep(1)
                print_s("\nYou are now wearing armour and will take less damage in combat!\n")
                potion = True
                armour = True
                armour_room()

            elif "back" in action or "leave" in action or "return" in action or "run" in action:
                print_s("You leave the treasure chest where it is and step out of the room.")
                frost_lich_room()

            else:
                print "Invalid. Try again."

def encounter_room1():

    print_s("\n~~~You are surprised by the silence of this room. You stop to listen...")
    print_s("You hear a faint noise...")
    time.sleep(2)
    randenc()


    while True:

        action = raw_input("\n> ")

        if action == "stats":
            stats()
            continue

        if "north" in action or "northern" in action:
            print_s("You approach the northern door. You hear noises from the other side.")
            encounter_room2()

        elif "south" in action or "southern" in action:
            print_s("You go through the southern door where the lich was.")
            frost_lich_room()

        elif "potion" in action:
            potion_drink()
            continue

        else:
            print "Invalid. Try again."

def encounter_room2():

        print_s("\n~~~You are hopeful this room does not have any surprises in store for you.")
        print_s("You hear a loud wheezing noise...")
        time.sleep(2)
        randenc()


        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "north" in action or "northern" in action:
                print_s("You approach the northern door and open it bravely.")
                beware_room()

            elif "south" in action or "southern" in action:
                print_s("You go back through the southern door even though you feel an overwhelming sense of dread.")
                encounter_room1()

            elif "potion" in action:
                potion_drink()
                continue

            else:
                print "Invalid. Try again."

def beware_room():

    print_s("\n~~~The walls of this room are made of bright white stone. You also see a large readable plaque on the floor. There are now doors to north, south and west. The northern door is made of steel that is so hot it turned red and is smoldering. The western door has a flaming shield symbol on it.  \nWhat do you do?")

    while True:

        action = raw_input("\n> ")

        if action == "stats":
            stats()
            continue

        if "potion" in action:
            potion_drink()
            continue

        if "inscription" in action or "read" in action or "plaque" in action:
            print_s("You kneel and get a closer look. The inscription reads in capital letters:")
            print_s("*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*")
            print_s(""" YOU HAVE ALMOST REACHED THE END OF THE DUNGEON. THE FINAL TEST LIES AHEAD OF YOU.  """)
            print_s("*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*")
            time.sleep(3)
            print_s("\nYou stand back up. You are afraid of what is behind the northern door.\n")
            time.sleep(3)
            print_s("You regain your courage. Which door do you try?")
            continue

        elif "north" in action or "northern" in action or "smoldering" in action or "wooden" in action:
            print_s("You gather a piece of cloth and push the smoldering steel door open with it.")
            time.sleep(1)
            fire_lich_room()

        elif "west" in action or "western" in action or "flaming" in action or "shield" in action or "symbol" in action:
            print_s("You push the door the western door that has a flaming shield on it and step in the room.")
            time.sleep(1)
            fire_ward_room()

        elif "south" in action or "southern" in action:
            print_s ("You start thinking going back is a bad idea.")
            time.sleep(1)
            encounter_room1()

        else:
            print "Invalid. Try again."

def fire_ward_room():

    global fire_ward
    global hp

    if not fire_ward:

        print_s("This room is also built with white stones. In the middle you see a pedestal with a floating scroll on it that is on fire. You feel very hot all of a sudden.")
        print_s("You know what this is. It's the fire ward scroll, and it looks similar to the frost ward scroll you saw earlier.")
        time.sleep(2)
        print_s("You approach the scroll expecting the worst.")
        time.sleep(2)
        print_s("The scroll reads: \"Only the blood of the worthy will gain our protection. All we ask for is five drops of blood.\"")
        time.sleep(1)
        print_s("What do you do?")

        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "potion" in action:
                potion_drink()
                continue

            elif "yes" in action or "Yes" in action or "fire" in action or "ward" in action or "take" in action or "give" in action or "blood" in action:
                print_s("You cut your palm and let five large drops of blood drip on the scroll.")
                fire_ward = True

                hp -= 5
                time.sleep(0.5)
                print "    \n#### YOU RECEIVE 5 DAMAGE ####\n"
                time.sleep(0.5)

                if hp <= 0:
                    death()

                print_s("You are now warded against fire magic!\n")
                time.sleep(1)
                fire_ward_room()

            elif "no" in action or "No" in action or "return" in action or "leave" in action or "back" in action:
                print_s("You are reluctant to give your blood and step out of the room.")
                beware_room()

            else:
                print "Invalid. Try again."

    if fire_ward:

        print_s("The fire ward scroll is now a pile of ashes on the pedestal. There is nothing of interest in this room. What do you do?")

        while True:

            action = raw_input("\n> ")

            if action == "stats":
                stats()
                continue

            if "potion" in action:
                potion_drink()
                continue

            if "door" in action or "back" in action or "return" in action or "leave" in action:
                print_s("You open the door and slam it behind you.")
                beware_room()

            else:
                print "Invalid. Try again."

def fire_lich_room():

    global fire_ward
    global fire_lich



    print_s("\n~~~As you enter you instantly feel a burning gaze upon you. You feel extreme heat in the room and cannot breathe. In front of you is the fire lich. A burning skull of death donning beautiful robes of red and white.")
    time.sleep(2.5)
    print_s("The fire lich casts a spell and creates an arena of fire around you and himself. You cannot escape.")
    print_s("The lich, spewing flames from his eyes and mouth screams:")
    time.sleep(1)
    print_s("\"You have reached the end, %s!\"" % name)
    time.sleep(1)
    print_s("\"....and by end I mean YOUR END! BWHA HA HA HA!\"")
    time.sleep(1)
    print_s("You are scared out of your mind. What do you do?")

    while True:

        action = raw_input("\n> ")
        condition = "attack" in action or "kill" in action or "fight" in action or "stab" in action or "destroy" in action or "fire" in action or "ward" in action

        if action == "stats":
            stats()
            continue

        if "potion" in action:
            potion_drink()
            continue

        if fire_ward and condition:
            print_s("You become a human torch. You are now blazing with fire and you feel powerful.")
            time.sleep(1)
            print_s("You and the lich fight almost as equals. Your attacks rip through the lich's essence damaging him tremendously.")
            print_s(". . .")
            time.sleep(2)
            print_s("The lich's attacks are powerful and you are hurt.")
            print_s(". . .")
            time.sleep(2)
            damage(20)
            print_s("\nYou destroy the fire lich.\n")
            fire_lich = False
            time.sleep(1)
            print_s("The lich screams as his body begins to disintegrate and then explode with a powerful bang. The room falls silent again.\n")
            time.sleep(1)
            print_s("A door opens, you can see the sunlight...peace.\n")
            time.sleep(2)
            end()


        elif not fire_ward and condition:
            print_s("You try to hit the lich but your attacks cause painful burns on your skin.")
            print_s("The lich laughs at you: \"PAH! You fool. You dare come here like other hundreds unprepared? You shall DIE!\"")
            print_s(". . .")
            time.sleep(2)
            damage(150)

        else:
            print "The lich instantly hurls a fireball that burns your face. It hurts badly."
            time.sleep(1)
            damage(25)

def end():

    print_s("     ###### YOU WIN THE GAME CONGRATULATIONS, %s !!!!!!! ######" % name)
    print_s("""  __      __.___ _______    _______  _____________________
/  \    /  \   |\      \   \      \ \_   _____/\______   \\
\   \/\/   /   |/   |   \  /   |   \ |    __)_  |       _/
 \        /|   /    |    \/    |    \|        \ |    |   \\
  \__/\  / |___\____|__  /\____|__  /_______  / |____|_  /
       \/              \/         \/        \/         \/ """)
    print_s("====================================================")
    print_s("Stockades is a text adventure game by Andrew Vatavu.")
    print_s("====================================================")
    raw_input("Press Enter to quit.")
    exit(0)


########### ROOMS ############

#def template():
     #delete this after eerything

    #action = raw_input("> ")

    #if action == "stats":ki
        #stats()
        # vezi daca trebuie definit stats ca fiind global
    #else:
        #print "ceau"

#15 dmg

start()



#potion_drink()
#frost_ward = True
#silverkey = True
#frost_ward = True

#frost_lich_room()
#prophecy_room()
#goblin2_room()
#torch = True
#goblin1_room()
#goblin1 = False
#prophecy_room()
