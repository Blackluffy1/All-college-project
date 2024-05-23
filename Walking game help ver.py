Xpos = 1 #sets players starting position
Ypos = 1 

Xlimit, Ylimit = 10, 10 #stops player walking off the map
Ymin, Xmin = 0, 0

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
    print("i'm not sure waht you meant by that ? ", command)

def userinput():
  command = input("what would you like to do?")
  if "walk" in command:
    getdirection(command)
  else:
     print("unknown command")
     userinput()



def getcoords(): #show the player where they are at 
  global Xpos
  global Ypos
  print("you are at",Ypos,Xpos)

def walknorth():
  global Ylimit , Ypos
  if Ypos < Ylimit:
    Ypos += 1
    print("you walk north")
    getcoords()
    userinput()
  else:
    print("a barrier blocks your path")
    userinput()

def walksouth():
  global Xpos , Ypos
  if Ypos < Ymin:
    Ypos -= 1
    print("you walk south")
    getcoords()
    userinput()
  else:
    print("a barrier blocks your path")
    userinput()

    
def walkwest():
  global Xpos , Ypos
  if Ypos < Ylimit:
    Xpos -= 1
    print("you walk west")
    getcoords()
    userinput()
  else:
    print("a barrier blocks your path")
    userinput()

def walkeast():
  global Ypos , Ymin,Xpos
  if Ypos < Ymin:
    Xpos += 1
    print("you walk east")
    getcoords()
    userinput()
  else:
    print("a barrier blocks your path")
    userinput()

    
userinput()    

    
  
