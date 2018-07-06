inventory = []
helpedlist = []
roomintros = ["Welcome to the land of kitties!\nAm I a kitty? Help me find out if I am a kitty:\nShould I:", "Welcome to the land of clouds!\nAm I a cloud? Help me find out if I am a cloud:\nShould I:", "Welcome to the land of stars!\nAm I a star? Help me find out if I am a star:\nShould I:", "Welcome to the land of flowers!\nAm I a flower? Help me find out if I am a flower:\nShould I:", "Welcome to the land of love hearts!\nAm I a love heart? Help me find out if I am a love heart:\nShould I:", "Welcome to the land of rainbows!\nAm I a rainbow? Help me find out if I am a rainbow:\nShould I:", "Welcome to the land of puppies!\nAm I a puppy? Help me find out if I am a puppy:\nShould I:", "You did it!"]
roomoptions = ["T = Talk to a kitty \nP = Play with a kitty\nL = Leave the kitties and go somewhere else","T = Talk to a cloud \nP = Play with a cloud\nL = Leave the clouds and go somewhere else", "T = Talk to a star \nP = Play with a star\nL = Leave the stars and go somewhere else", "T = Talk to a flower \nP = Play with a flower\nL = Leave the flowers and go somewhere else","T = Talk to a love heart \nP = Play with a love heart\nL = Leave the love hearts and go somewhere else", "T = Talk to a rainbow \nP = Play with a rainbow\nL = Leave the rainbows and go somewhere else","T = Talk to a puppy \nP = Play with a puppy\nL = Leave the puppies and go somewhere else"]
talkoptions = ["I have pointy claws that can give you sores but I have no fire to warm me... \nCan you give me some warmth?","I have the strength to fly up high in the sky, but no fluff to puff me... \nCan you give me come fluff?","I have so much heat I could burn off your feet, but my shine has but all but left me... \nCan you give me some shine?", "I have colours that mellow to the brightest of yellow, but my stem lacks the strength to hold me...\n Can you give me some strength?", "I am bursting with love as pure as a dove, but have nothing sharp to pierce me... \nCan you give me something sharp?", "I am so bright I am but made from light, but without colours you cant't see me... Can you give me some colour?", "My coat has so much fluff, you would call it a bluff, but I have no-one to love me... Can you give me some love?"]
giveoptions = ["Y = Yes, take some of my warmth and be happy\nN = No, I have no warmth to give. I'm sorry.","Y = Yes, take some of my fluff and be happy\nN =  No, I have no fluff to give. I'm sorry.", "Y = Yes, take some of my shine and be happy \nN = No, I have no shine to give. I'm sorry.", "Y = Yes, take some of my strength and be happy \nN = No, I have no strength to give, I'm sorry","Y = Yes, take my pointy nail and be happy \nN = I have nothing sharp to give, I'm sorry","Y = Yes, take some colours and be happy \nN = No, I have no colours to give. I'm sorry", "Y = Yes, take some love and be happy \nN = No, I have no love to give. I'm sorry"]
thankyoulist = ["I am so warm and cosy, oh thank you so much! Please take more pointy claws, may it they you good luck!", "I am fluffy and puffy, oh thank you so much! Please take some of my strength, may it give you good luck!", "I am shiney and brighty, oh thank you so much! Please take some of my warmth, may it give you good luck!","I am standing upright, oh thank you so much! Please take some of my colour, may it give you good luck!","My love is now all to feel, oh thank you so much! Please take some of my love, may it give you good luck!","I am so colourful, oh thank you so much! Please take some of my light, may it give you good luck!","I am so loved and happy, oh thank you so much! Please take some of my fluff, may it give you good luck!"]
playresponses = ["The kitties jump and they chase but can't catch you. You fly too high to be a kitty.","The clouds do fly up in the sky, but they are full of water. You are too solid to be a cloud.","The stars shine bright up in the sky, but they are too hot to touch. You are too cool to be a star.","The flowers grow taller in the sun, but they do not eat as you do. You are too animalistic to be a flower.","The love heart is lovely and plush, but they do not light up as you do. You are too bright to be a love heart.","The rainbow is long and curvy but has just two legs to stand on. You have too many legs to be a rainbow.","The puppy is warm and soft and round, but is so big it nearly squashed you. You are too small to be a puppy."]
gifts = ["pointy nail","strength","warmth","colour","love","light","fluff"]
needs = ["warmth","fluff","shine","strength","pointy nail","colours","love"]
directionvalues = [0,1,5,0,-1,0,1,0,3,0,1,-1,1,0,0,-1,0,-1,0,1,1,-3,-1,-5, 1,-1,0,0,]

x=0



def directionFunc(x):
    while True:
        while x < 7:
            direction = input("Please select the direction you want to go (N/S/E/W): ")
            if direction == "n" or direction == "N":
                directionchoice = directionvalues[x*4]
                if directionchoice == 0:
                    print("Uh oh, you can't go in this direction! Please try another direction.")
                    continue
                else:
                    x = x + directionchoice
                    return x
            elif direction == "s" or direction =="S":
                directionchoice = directionvalues[x*4+1]
                if directionchoice == 0:
                    print("Uh oh, you can't go in this direction! Please try another direction.")
                    continue
                else:
                    x = x + directionchoice
                    return x
            elif direction == "e" or direction =="E":
                directionchoice = directionvalues[x*4+2]
                if directionchoice == 0:
                    print("Uh oh, you can't go in this direction! Please try another direction.")
                    continue
                else:
                    x = x + directionchoice
                    return x
            elif direction == "w" or direction =="W":
                directionchoice = directionvalues[x*4+3]
                if directionchoice == 0:
                    print("Uh oh, you can't go in this direction! Please try another direction.")
                    continue
                else:
                    x = x + directionchoice
                    return x
            else:
                print("Uh oh, I don't know what that means. Please enter N, S, E or W.")
                continue
        while x == 7:
            if set([0,1,2,3,4,5,6]).issubset(set(helpedlist)):
                print: ("You did it!\nYou are loving and warm, with just the right amount of fluff,\nBut also strong, and sharp and all that good stuff!\nYou shine brighter than the sun, with all the colours of the sky,\nYou made sad things happy, you are a firefly! ")
                break
            else:
                print("There are still unhappy things out there! You need to visit every world before getting through this door.")
                break



 


def roomFunc():
    global x
    print(roomintros[x])
    while x < 7:
        print(roomoptions[x])
        choice = input("Please enter your choice: ")
        if choice =="T" or choice == "t":
            print(talkoptions[x])
            print(giveoptions[x])
            choice1 = input("Please enter your choice: ")
            if choice1 == "y" or choice1 == "Y":
                if gifts[x] in inventory:
                    print(thankyoulist[x])
                    helpedlist.append(x)
                    inventory.append(gifts[x])
                    print("You have gained ",gifts[x])
                    print("You no longer have",needs[x])
                    del needs[x]
                else:
                    print("You have no ",needs[x]," to give. Try exploring some more worlds!")
            elif choice1 == "n" or choice1 == "N":
                print("That's okay, but please do come back should you have some ",needs[x]," to spare.")
                continue
            else:
                print("Uh oh, I don't know what that means! Please try again.")
                continue
        elif choice =="P" or choice == "p":
            print(playresponses[x])
            continue
        elif choice =="L" or choice =="l":
            x = directionFunc(x)
            continue
     
      
            
           
    
def main():
    while True:
        print("I don't know what I am, can you help me?:\nY = Yes! I'd love to help.\nN = No, I'm sorry, I can't help you right now.")
        entergame = input("Please enter answer: ")
        if entergame == "Y" or entergame == "y":
            roomFunc()
            
        elif entergame == "N" or entergame == "n":
            print("Goodbye!")
            break 
        else:
            print("Uh oh, I don't know what that means! Please try again.")
            continue

main()

