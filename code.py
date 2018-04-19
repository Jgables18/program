import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import sys, tty, termios, signal

# definitions 

def stopAll():
    pass

def open():
    RPL.servoWrite(0,500)
    RPL.servoWrite(1,2500)
    print "open"
		
def stepopen():
    RPL.servoWrite(0,RPL.servoRead(0)-5)
    RPL.servoWrite(1,RPL.servoRead(1)+5)
    print "step open"
		
def bigstepopen():
    RPL.servoWrite(0,RPL.servoRead(0)-20)
    RPL.servoWrite(1,RPL.servoRead(1)+20)
    print "big step open"

def close():
    RPL.servoWrite(0, 1000)
    RPL.servoWrite(1, 2000)
    print "close"
		
def stepclose():
    RPL.servoWrite(0,RPL.servoRead(0)+5)
    RPL.servoWrite(1,RPL.servoRead(1)-5)
    print "step open"

def bigstepclose():
    RPL.servoWrite(0,RPL.servoRead(0)+20)
    RPL.servoWrite(1,RPL.servoRead(1)-20)
    print "big step open"

def show():
    print ("left Motor is at", RPL.servoRead(0))
    print ("Right Motor is at", RPL.servoRead(1))
		
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

def interrupted(signum, frame):
  	stopAll()

signal.signal(signal.SIGALRM, interrupted)
tty.setraw(sys.stdin.fileno())

print "Ready To Grab! Press * to quit.\r"

SHORT_TIMEOUT = 0.255

while True:
	signal.setitimer(signal.ITIMER_REAL,SHORT_TIMEOUT)
	ch = sys.stdin.read(1)
	signal.setitimer(signal.ITIMER_REAL,0)
	
if ch == '*':
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    break
	
  	else
    if ch == 'q':
      open()
    elif ch == 'a':
      stepopen()
    elif ch == 'z':
      bigstepopen()
    elif ch == 'w':
      close()
    elif ch == 's':
      stepclose()
    elif ch == 'x':
      bigstepclose()
    elif ch == 'p':
      show()    
    else:
      stopAll()
