import curses
import textwrap

def splitAndPad(text,width):
  ans = textwrap.wrap(text,width)
  for i in range(len(ans)):
    ans[i] += ' '*(width-len(ans[i]))
  return ans

def addStatus(text):
  for t in splitAndPad(text,STATUS_WIDTH):
    statusPad.addstr(screenH-6,1,t)
    statusPad.scroll(1)
  statusPad.border(0)
  statusPad.refresh()

def addMessage(text,sender,time):
  messages.append(splitAndPad(time+" - "+sender+':',screenW-STATUS_WIDTH-4)[0])
  for t in splitAndPad(text,screenW-STATUS_WIDTH-4):
    messages.append(t)

def scrollMessages(scroll):
  global lastDisplayMessage
  lastDisplayMessage += scroll
  lastDisplayMessage = min(-1,max(lastDisplayMessage,-len(messages)+screenH-7))
  updateMessageScreen()

def updateMessageScreen():
  global lastDisplayMessage
  messagePad.erase()
  for i,m in enumerate(messages[max(-len(messages),lastDisplayMessage-screenH+8):lastDisplayMessage] + [messages[lastDisplayMessage]]):
    messagePad.addstr(i+1,1,m)
  messagePad.border(0)
  messagePad.refresh()


def cleanup():
  screen.keypad(0)
  curses.echo()
  curses.endwin()

STATUS_WIDTH = 10

messages = ['']
lastDisplayMessage=  -1

currentMessage = []
lastDisplayCurrentMessage = -1

screen = curses.initscr()
screen.keypad(1)
screen.timeout(1)
curses.noecho()

screenH,screenW = screen.getmaxyx()
STATUS_WIDTH = max(STATUS_WIDTH,screenW/3)

screen.addstr(0,screenW-STATUS_WIDTH-1,"STATUS")
statusPad = screen.subpad(screenH-5,STATUS_WIDTH+2,1,screenW-STATUS_WIDTH-2)
statusPad.border(0)
statusPad.scrollok(1)
statusPad.idlok(1)

screen.addstr(0,1,"MESSAGES")
messagePad = screen.subpad(screenH-5,screenW-STATUS_WIDTH-2,1,0)
messagePad.border(0)
messagePad.scrollok(1)
messagePad.idlok(1)
screen.refresh()
