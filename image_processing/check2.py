import Leap, sys, math
from Leap import *
import socket

direction = "0"
forward = "0"

total_data = ""


host = "192.168.10.4"
port = 5444
buf = 2
ADDR = (host, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


class LeapMotionListener(Leap.Listener): 
  past_hands = []
  count_down = 0
  
  def on_init(self, controller):
    print "Initialized"
    

  def on_connect(self, controller):
    print "Connected"
    

  def on_disconnect(self, controller):
    print "Disconnected"

  def on_frame(self, controller):

    #Check to see if the Leap Motion senses a hand
    frame = controller.frame()
    hands = frame.hands

    global direction
    global forward
    global backward
    global total_data

    global host
    global port
    global buf
    global ADDRc

    global client

    for hand in frame.hands:

      handType = "Left hand" if hand.is_left else "Right hand"
      if(handType=="Right hand") : 
        #print "Right"
        if (hand.grab_strength==0):
            #print "Paper"
            hand_center = hand.palm_position
            handx = hand_center.x

            dist = hand_center.y

            #not consider acc 
            if(dist<=160):
              forward = "0" #print "fast forward"  
            elif(160<dist<=330):
              forward = "1"  #print "slow forward"
            elif(330<dist<=340):
              forward = "5" #print "stop region"
            elif(340<dist<=550):
              forward = "2"  #print "slow backward"
            else :
              forward = "3"  #print "fast backward"

            if handx <= (-100):
              direction = "0"  #left left
            elif handx <= (-35):
              direction = "1"  #left 
            elif handx <= 35:
              direction="2"   #center
            elif handx <= 100:
              direction = "3" #right
            elif handx > 100:
              direction = "4" #right right

        elif (hand.grab_strength == 1):
            forward = "4"      #Stop the Car

            hand_center = hand.palm_position
            handx = hand_center.x

            if handx <= (-100):
              direction = "0"
            elif handx <= (-35):
              direction = "1"
            elif handx <= 35:
              direction="2"
            elif handx <= 100:
              direction = "3"
            elif handx > 100:
              direction = "4"

      total_data = forward + direction
      client.send(total_data.encode())

def main():
    # Create a sample listener and controller
    listener = LeapMotionListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
