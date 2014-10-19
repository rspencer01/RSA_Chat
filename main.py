import curses
import ui
import os
import messages
import comms
from messages import message

username,password = '',''

def loadMessagesFromFile(directory):
  ui.addStatus("Loading old messages")
  for msg in messages.loadAllMessages():
    ui.addMessage(msg)
  ui.updateMessageScreen()

def sendMessage(text):
  ui.addStatus("Sending message")
  comms.sendMessage(text)
  mesg = message(text,sender=username)
  mesg.saveToFile()
  ui.addMessage(mesg)
  ui.updateMessageScreen()

def processInput(inp):
  if inp=='':return
  if inp[0]!='\\':
    sendMessage(inp)
  elif len(inp)>=7 and inp[:7] == '\server':
    comms.startServer()
  elif len(inp)>=7 and inp[:7] == '\client':
    comms.startClient(inp.split()[1],int(inp.split()[2]))
    
def receiveMessage(data):
  ui.addStatus("Receiving message")
  mesg = message(data)
  mesg.saveToFile()
  ui.addMessage(mesg)
  ui.updateMessageScreen() 
  
  
if __name__=="__main__":
  username,password = ui.getLogin()

  loadMessagesFromFile('messages/')

  buff=''
  while 1:
    ui.screen.addstr(ui.screenH-3,0,' '*(ui.screenW-4))
    ui.screen.addstr(ui.screenH-3,0,'>'+buff)  
    
    nxt = comms.getNextMessage()
    if nxt:
      receiveMessage(nxt)
    
    a = ui.screen.getch()
    if a==-1:
      continue
    if a==27:
      break
    elif a==curses.KEY_UP:
      ui.scrollMessages(-1)
    elif a==curses.KEY_DOWN:
      ui.scrollMessages(1)
    elif a==10:
      processInput(buff)
      buff=''
    elif a==8 or a==265:
      if buff!='':
        buff = buff[:-1]
    else:
      buff += chr(a)


  ui.cleanup() 
  comms.cleanup()
