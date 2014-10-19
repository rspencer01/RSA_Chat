from time import strftime
import os

class message:
  def __init__(self,message='',sender='',time=strftime('%Y-%m-%d %H-%M-%S')):
    self.message = message
    self.time = time
    self.sender = sender
  def loadFromFile(self,fn):
    f = open('messages/'+fn,'r')
    lines = f.readlines()
    self.time = lines[0]
    self.sender = lines[1]
    self.message = ''.join(lines[2:])
    f.close()
  def saveToFile(self,fn=None):
    if fn==None: fn = self.time
    f = open('messages/'+fn,'w')
    f.write(strftime('%Y-%m-%d %H:%M:%S')+'\n')
    f.write(self.sender+'\n')
    f.write(self.message)
    f.close()

def loadAllMessages():
  ans = []
  for fn in os.listdir('messages'):
    ans.append(message())
    ans[-1].loadFromFile(fn)
  return ans
