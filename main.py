import curses
import ui
import os
import messages
from messages import message

username,password = '',''

def loadMessagesFromFile(directory):
  ui.addStatus("Loading old messages")
  for msg in messages.loadAllMessages():
    ui.addMessage(msg)
  ui.updateMessageScreen()

def sendMessage(text):
  mesg = message(text,sender=username)
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
      sendMessage(buff)
      buff=''
    elif a==8:
      if buff!='':
        buff = buff[:-1]
    else:
      buff += chr(a)
    ui.screen.addstr(ui.screenH-3,0,' '*(ui.screenW-4))
    ui.screen.addstr(ui.screenH-3,0,'>'+buff)

  ui.cleanup() 
