import socket
import select
import ui

# Our socket
sock = None
server = False
# Contains our socket and the other person's socket
SOCKET_LIST = []

def startServer(port=8000):
  global sock,server
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind(('', port))
  sock.listen(10)  
  SOCKET_LIST.append(sock)
  ui.addStatus("Started as server on %s:%s" % sock.getsockname())
  server = True
  RECV_BUFFER = 4096 

def startClient(host='localhost',port=8000):
  global sock
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(2)
  sock.connect((host,port))
  SOCKET_LIST.append(sock)
  ui.addStatus("Started as client")
  
def sendMessage(msg):
  SOCKET_LIST[-1].send(msg)
  
def getNextMessage():
  # No sockets means nothing to do
  if SOCKET_LIST==[]:
    return None
    
  # Use select to see if any sockets are ready to read
  ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)

  # Loop through them all
  for sockt in ready_to_read:
      # a new connection request recieved
      if sockt == sock and server: 
          sockfd, addr = sock.accept()
          ui.addStatus("Client (%s, %s) connected" % addr)
          SOCKET_LIST.append(sockfd)
      else:
        data = sockt.recv(1000)
        return data
  return None
      
def cleanup():
  if sock:
    sock.close()
