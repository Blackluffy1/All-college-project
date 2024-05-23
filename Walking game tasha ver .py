import random
import time
import sys




xlimit, ylimit = 10, 10 #stops player walking off the map
ymin, xmin = 0, 0

xpos = 1 #sets players starting position
ypos = 1 
inventory = "nothing"


item_weapons  =  (["sword","claymore","spear","shield"])
item_clothing = (["leather pants","leather cap","leather shoes ","leather shirt"])
item_food = (["steak","cheese","bread","pancakes"])
full_item = (["sword","claymore","spear","shield", "leather pants","leather cap","leather shoes ","leather shirt", "steak","cheese","bread","pancakes"])

def getdirection(command):
  if "north" in command:
    walknorth()
  elif "east" in command:
    walkeast()
  elif "south" in command:
    walksouth()
  elif "west" in command:
    walkwest()
  else:
    print("i'm not sure what you meant by that ? ", command)
    userinput()
    getdirection(command)

def userinput(): #A function to control user input
  #Take input from user
  command = input(" what would you like to do ? ")
  print("Hint: you can go North,East,South,West")
  print("Hint: to use inventory to see your inventory)\n")
  print("                                               ")
  if "walk" in command: #If the user walked
    getdirection(command) #Figure out which direction they wanted
    userinput()
  elif command == "inventory": #Command to allow the user to see their 
    print("                      ")
    print(inventory,"in inventory")
    userinput()
    
  else:
    print("Unknown command.") #for unregistered commands 
    userinput()
      
      
    
def location():
   global xpos
   global ypos
   print("you are at",xpos ,ypos)
   location()

def inventory_system(): 
  answer = input("you have found an item would you like to pick up the item ? ")
  print("                 ")
  if answer == "yes" :
    randomised = random.choice(full_item)
    print("you pick up the item", randomised)
    print ("you now have",randomised,"in your inventory ")
    randomised = inventory 



def checkCoords():
  if ypos == 5 and xpos == 5 :
    inventory_system()
    
  

def getcoords(): #show the player where they are at 
  global xpos
  global ypos
  print("you are at",xpos,ypos)
  

def walknorth():
  global ylimit , ypos
  if ypos < ylimit:
    ypos += 1
    print(name," walks north")
    getcoords()
    checkCoords()
    userinput()
  else:
    print("a barrier blocks your path")
    userinput()
    

def walksouth():
  global ypos , ymin
  if ymin < ypos:
    ypos -= 1
    print(name,"walks south")
    getcoords()
    checkCoords()
    userinput()
  else:
    print("a barrier blocks your path")
    userinput()
    

def walkwest():
  global xpos ,xmin
  if xmin < xpos:
    xpos -= 1
    print(name,"walk west")
    getcoords()
    checkCoords()
    userinput()
  else:
    print("a barrier blocks your path")
    userinput()
    

def walkeast():
  global xpos , xlimit
  if xpos < xlimit:
    xpos += 1
    print(name,"walks east")
    getcoords()
    checkCoords()
    userinput()
  else:
    print("a barrier blocks your path")
    userinput()
    

    
      
print ( "hello welcome to sword art online death here means death in the real world !!!")
print("                                                        ")
print("""          ╔╦╦╦═╦╗╔═╦═╦══╦═╗
          ║║║║╩╣╚╣═╣║║║║║╩╣
          ╚══╩═╩═╩═╩═╩╩╩╩═╝
""")
print("                                         ")
name = input("SAO adventurer what is your name? ")
print("                                                          ")
print (" wow what a beautiful !!!!")
print("                                                                     ")
print("""_______                         
 \      \ _____    _____   ____  
 /   |   \\__  \  /     \_/ __ \ 
/    |    \/ __ \|  Y Y  \  ___/ 
\____|__  (____  /__|_|  /\___  >
        \/     \/      \/     \/ 
               """)
print("                                                                     ")
print("Anyway sorry adventurer",name,"I get a bit excited but   only enter which direction once dialogue has ended")
print("                                                          ")
print(name,"please enter which direction you would like to walk  ")
print("                                                          ")
print("options : walk west ,walk south,walk east,walk north ")
print("                                                     ")
print(" so much choice oh where to go ????? ")
print("                                ")
print("dialogue has ended !!!!")
print("                       ")
for x in name:
  sys.stdout.write(x)
  sys.stdout.flush()
  time.sleep(0.2)
userinput()

