import curses
import ui


if __name__=="__main__":
  buff=''
  while 1:
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
      ui.sendMessage(buff)
      buff=''
    elif a==263:
      if buff!='':
        buff = buff[:-1]
    else:
      buff += chr(a)
    ui.screen.addstr(ui.screenH-1,0,' '*(ui.screenW-4))
    ui.screen.addstr(ui.screenH-1,0,'>'+buff)

  ui.cleanup() 
