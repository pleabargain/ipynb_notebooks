import random
import time

def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    #define the variable cave
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        #user has to choose between 1 or 2
        #otherwise it just loops...
        #a loop that only accepts two possible answers
        #how to take advantage of this?
        cave = input()
    #only appears in def-blocks
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    #be nice to display an image here...
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)
    #randomly choose life of death
    #but what does the 1,2 do?
    friendlyCave = random.randint(1, 2)
    #convert the int to a str
    if chosenCave == str(friendlyCave):
         print('Gives you his treasure!')
    else:
         print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    #run this function
    displayIntro()
    #do these functions have to be in the same script?
    #can I pull them from the same folder?
    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
