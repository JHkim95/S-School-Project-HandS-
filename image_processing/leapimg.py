import Leap, sys, math
from Leap import *
import socket

left_3 = 90
left_2 = 50
left_1 = 30

right_3 = 90
right_2 = 50
right_1 = 30

direction = "00"
forward = "00"
backward = "00"
breaker = "00"
total_data = ""


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
    global breaker
    global total_data
  
    for hand in frame.hands:
      handType = "Left hand" if hand.is_left else "Right hand"
      if(handType=="Left hand") : 
        if hand:
          if (hand.grab_strength==0):
            #print "Paper"
            breaker = "00"
            hand_center = hand.palm_position
            dist = hand_center.y

            #not consider acc 
            if(dist<=110):
              #print "forward"
              forward = "+1"
              backward = "00"
            else :
              #print "backward"
              forward = "00"
              backward = "+1"

          if (hand.grab_strength==1):
            #print "Rock"
            breaker = "+1"
      else :
        #print "Right"
        if (hand.grab_strength==0):
            #print "Paper"
            hand_center = hand.palm_position
            newx = hand.palm_position.x-140
            newy = hand.palm_position.y-115
            newvector = Vector(newx, newy, hand.palm_position.z)
            roll = newvector.roll*Leap.RAD_TO_DEG
            if(roll>0):
              #print "Right"
              roll1 = 180-roll
              if(roll1<=right_1):
                direction = "-1"
              elif(right_1<roll1<=right_2):
                direction = "-2"
              elif(right_2<roll1):
                direction = "-3"
              else:
                direction = "00"
            else:
              #print "Left"
              roll2 = 180+roll
              if(roll2<=left_1):
                direction = "+1"
              elif(left_1<roll2<=left_2):
                direction = "+2"
              elif(left_2<roll2):
                direction = "+3"
              else:
                direction = "00"
      total_data = forward + backward + direction + breaker
      print total_data
      #client.send(total_data.encode())
      

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


