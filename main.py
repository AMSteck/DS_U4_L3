#Alannah Steck
#U4L3
#file reverse
#૮꒰ ˶• ༝ •˶꒱ა  Good Luck Bunny
from StackClass import ArrayStack
with open("earnest.txt",'r') as openFile:
  contents = openFile.read()

def main():
  new = ""
  for item in contents:
    x = ord(item)
    if x == 32 or x<91 and x>64 or x<123 and x>96:
      new+=item
  new = new.split()
  newStack = ArrayStack()
  for item in new:
    newStack.push(item)
  newest = ""
  for item in range(len(newStack)):
    addThis = newStack.pop()
    newest += f"{addThis} "
  with open("reverse.txt",'w') as openFile:
    openFile.write(newest)
    

if __name__ == "__main__":
  main()