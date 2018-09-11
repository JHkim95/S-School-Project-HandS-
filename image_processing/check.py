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


host = '192.168.0.8'
port = 5050
buf = 8
ADDR = (host, port)

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(ADDR)



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

    global host
    global port
    global buf
    global ADDR

    global client


    """
    
    파이썬 코드 바꿔놓으면 그거 맞춰서 웹 코드 바꿔놓겠습니다.
    속도 추가 하실거면 하시면 됩니다.
      - 왼손 위치에 따라서 전진/후진 + 속도 이런식?!
      - 하게 되면 주석으로 속도 값 써주세요.


    가장 바깥 for문은 변경하지말고 안에 있는 값들만 바꿀 것.
    
    변수 설명 
    hand.is_left ==> 왼손이면 T, 오른손이면 F
    hand_center = hand.palm_position ==> 손바닥 중앙 값 
    hand_center.x ==> 손바닥 중앙값의 x값.
    hand_center.y ==> 손바닥 중앙값의 y값.
    hand_center.z ==> 손바닥 중앙값의 z값.    
      *https://developer-archive.leapmotion.com/documentation/v2/python/api/Leap.Vector.html 에서 x, y, z 축 확인할 것.
      *현재 x와 y값만 이용해서 판단.
      
    hand.grab_strength ==> 1이면 주먹 쥔 것, 아니면 핀 것.
   
    """
  
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
            if(dist<=100):
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
            forward = "00"
            backward = "00"
      else :
        #print "Right"
        if (hand.grab_strength==0):
            #print "Paper"
            hand_center = hand.palm_position
            handx = hand_center.x
            #newx = hand.palm_position.x-50
            #newy = hand.palm_position.y-95
            if handx<=51 :
              direction = "-3"
            elif handx<=72:
              direction = "-2"
            elif handx<=93:
              direction="-1"
            elif handx<=114:
              direction = "00"
            elif handx<=135:
              direction = "+1"
            elif handx<=157:
              direction ="+2"
            elif handx<=190:
              direction ="+3"


            #newvector = Vector(newx, newy, hand.palm_position.z)
            #roll = newvector.roll*Leap.RAD_TO_DEG
            #roll2 = hand_center.roll

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


