import time
import math
rpSChild = 0
def letsPlay():
  print("yay")

def shovelTalkChild():
  print("Uhm, so turns out that was actually a test to see if you were a decent guy.")
  time.sleep(3)
  print("my bad guys..")
  time.sleep(1)
  print("Anyways, they sedated you and froze you 'till someone could take you back to a normal research center,")
  time.sleep(4)
  print("Which was a liiiitttlleeee too long,")
  time.sleep(2)
  print("So like when they unfroze you, they couldn't wake you up-")
  time.sleep(1)
  print("Again, my bad.")
  time.sleep(1)
  print("YOU DIED")
  quit()

def relationshipPointsIntro():
   time.sleep(4)
   print(".")
   time.sleep(1)
   print(".")
   time.sleep(1)
   print(".")
   time.sleep(1)
   print(".")
   time.sleep(1)
   print("INTRODUCING: RELATIONSHIP POINTS!")
   time.sleep(2)
   print("Right now, your points for the child are at..." + rpSChild)
   time.sleep(2)
   print("Depending on that for each character, a different thing will happen.")
   time.sleep(2)
   print("Basically, more or less information.")
   time.sleep(2)
   print("Whenever you're alone, just type 'Relationships' to check any one of them.")
   time.sleep(3)
   print("Thats it.")
   time.sleep(1)
   print(".")
   time.sleep(1)
   print(".")
   time.sleep(1)
   print(".")
   time.sleep(1)
   print(".")
   if rpSChild > 0:
    letsPlay()
   else:
    shovelTalkChild()

def sureThing():
   print("The child let out a shriek of happiness and skipped away to grab something.")
   time.sleep(3)
   print("Wonderful.")
   time.sleep(1)
   print("Anyways, now that you are alone, I can teach you a 'lil something.")
   rpSChild + 1
   relationshipPointsIntro()



def hellNaw():
   print("The child pouted and sped off suddenly, leaving you in the dust.")
   time.sleep(3)
   print("How peculiar.")
   time.sleep(1)
   print("Alrighty then, now that you're actually awake for once, we can get some learning in.")
   rpSChild - 1
   relationshipPointsIntro()

def iPolite():
   nopeSure = ["Nope", "nope", "Sure", "sure"]
   print("'Please be quiet,' you mutter in your half-asleep daze, at least you had the courtesy to use please.")
   time.sleep(2)
   print("I personally would've jumped out of my bed and smacked the person multiple times.")
   time.sleep(2)
   print("Anyways, the perpetrator appears to get closer. They walk loudly, and they appear to be skipping towards you.")
   time.sleep(2)
   print("The nuisance peers over, and you notice that the figure appears to be quite young.")
   time.sleep(2)
   print("'Hellooooo?' The child waves their hand above your face.")
   time.sleep(1)
   print("You don't have much energy, but you should probably respond:")
   hiChild = input()
   print("'" +hiChild+ "'")
   time.sleep(3)
   print("'Oh wow! You're actually not dead!' The child retreats from your face, standing next to the bed.")
   time.sleep(3)
   print("'Anyways, welcome! It will probably take time for you to get out of bed, which will probably be super borrringggg")
   print("'Butttttt, that also means you can play with me!'")
   print("You can choose to say sure or nope:")
   userInput = ""
   while userInput not in nopeSure:
       print("Say sure or forever hold your peace.")
       userInput = input()
       if userInput == "Sure":
         time.sleep(2)
         sureThing()
       elif userInput == "Nope":
         time.sleep(2)
         hellNaw()
       elif userInput == "nope":
         time.sleep(2)
         hellNaw()
       elif userInput == "sure":
         time.sleep(2)
         sureThing()
       else:
           print("The child took that as a yes.")
           time.sleep(2)
           sureThing()


def iScream():
   print("'SHUT UP!!' you hopped out of the clinical bed, ripping out an IV you didn't know was there and use your blurry sight to track down who was screaming.")
   time.sleep(3)
   print("Just as you raised your hand to beat the crap out of the perpetrator, you pass out from the sudden movement. It was too much for your still-weak body.")
   time.sleep(3)
   print("YOU DIED")
   quit()


def speakSpeakSleep():
   screamPolite = ["scream", "polite"]
   print(".")
   print(".")
   print(".")
   print(".")
   time.sleep(2)
   print("'GOOD MORNING " + name + "!!!!!' Someone shouts at you.")
   time.sleep(1)
   print("The blaring sound of someone cuts through your beauty sleep.")
   time.sleep(2)
   print("Now you have two choices:")
   time.sleep(2)
   print("You can scream at this voice to shut up (as you should honestly)")
   time.sleep(3)
   print("or politely tell them to be quiet.")
   time.sleep(1)
   print("To scream, type scream, and for polite no, type polite:")
   userInput = ""
   while userInput not in screamPolite:
       userInput = input()
       if userInput == "scream":
           iScream()
       elif userInput == "polite":
           iPolite()
       else:
           print("The agony of the screaming gets to you.")
           time.sleep(1)
           print("YOU DIED.")
           quit()


def speakSpeak():
   print("You muster up enough strength to talk, and you can say one thing:")
   firstWords = input()
   print("'" +firstWords+ "'")
   time.sleep(3)
   print("You hear a gasp coming from the sillhouette.")
   print("'Oh my goodness, you're awake!'")
   time.sleep(1)
   print("'I was honestly starting to think that you would never wake up!")
   time.sleep(3)
   print("'I'm Raia, an intern here! You're in [////////] research center!'")
   time.sleep(3)
   print("'Do you need water or anything?'")
   time.sleep(3)
   print("'..No.' You manage to croak out.")
   time.sleep(3)
   print("'Alright, make sure to get some rest! We can talk next time you wake, you look pretty pale.")
   time.sleep(3)
   print("You fall back asleep. It is dreamless and lonely, but at least you aren't drowning.")
   time.sleep(3)
   speakSpeakSleep()






def backToSleep():
   print("You go back to sleep. You don't wake up.")
   import time
   time.sleep(1)
   print("You fool. Wasting your chance.")
   time.sleep(1)
   print("YOU DIED.")
   quit()


def introScene():
   introYesNo = ["Yes", "No", "yes", "no"]
   import time
   print("You wake up in a clinic of sorts. The air smells stertile in a way you haven't witnessed since the disaster.")
   time.sleep(5)
   print("Your vision is slightly blurry, and you feel very wet. Your mind goes back to when you drowned.")
   time.sleep(3)
   print("You shudder. You dont want to go back to that again.")
   time.sleep(3)
   print("Out of the corner of your eye, you see a figure.")
   time.sleep(3)
   print("Where even are you anyways? Apart from knowing you're in a clinic with some strange.. person? you have no idea where you are.")
   time.sleep(4)
   print("Should you say something?")
   userInput = ""
   while userInput not in introYesNo:
       print("Don't be indecisive. Yes or No?")
       userInput = input()
       if userInput == "Yes":
         speakSpeak()
       elif userInput == "No":
           backToSleep()
       elif userInput == "no":
           backToSleep()
       elif userInput == "yes":
           speakSpeak()
       else:
           print("You indecisive fool.")
           print("YOU DIED.")
           quit()
# i love you.
if __name__ == "__main__":
   while True:
       print("Welcome, traveler!")
       time.sleep(2)
       print("It appears as you have drowned.")
       time.sleep(2)
       print("Though, I have decided to save you instead of letting you pass on in the current.")
       time.sleep(3)
       print("But before I do as such, I will need your name:")
       name = input()
       time.sleep(1)
       print("I hope you enjoy this second chance, " +name+ ".")
       time.sleep(2)
       introScene()
# i eat cars haha im so amazing
