import Leap, sys, math
from Leap import *
import socket
from Leap import CircleGesture


direction = "0"
forward = "0"

total_data = ""


host = '192.168.1.103'
port = 5104
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
    controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

    controller.config.set("Gesture.Circle.MinRadius", 10.0)
    controller.config.set("Gesture.Circle.MinArc", .5)
    controller.config.save()

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

    global host
    global port
    global buf
    global ADDRc

    global client

    """
    for gesture in frame.gestures():
      if gesture.type != Leap.Gesture.TYPE_CIRCLE :
        print("F")
      else:
        circle = CircleGesture(gesture)
        print("T")
    """

    for hand in frame.hands:

      handType = "Left hand" if hand.is_left else "Right hand"
      if(handType=="Right hand") : 
        #print "Right"
        if (hand.grab_strength==0):
            #print "Paper"
            hand_center = hand.palm_position
            handx = hand_center.x
            #newx = hand.palm_position.x-50
            #newy = hand.palm_position.y-95
            dist = hand_center.y

            #not consider acc 
            if(dist<=180):
              #print "forward"
              forward = "0"  
              #backward = "00"
            elif(180<dist<=380):
              forward = "1"  
            elif(380<dist<=400):
              forward = "5"
            elif(400<dist<=520):
              #print "backward" 
              forward = "2"  
              #backward = "+1" 
            else :
              forward = "3"  

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

        elif (hand.grab_strength == 1):
            forward = "4"

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
            #newvector = Vector(newx, newy, hand.palm_position.z)
            #roll = newvector.roll*Leap.RAD_TO_DEG
            #roll2 = hand_center.roll

      total_data = forward + direction
#      print total_data
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
