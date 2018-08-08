import servo_test
import motor
from socket import *
import time

def init():
    print("a")
    motor.setup()
    servo_test.setup()
    motor.setSpeed(20)
    servo_test.pwm.write(0,0,240)

HOST = "192.168.1.105"
PORT = 5000
BUFSIZE = 8
ADDR = (HOST, PORT)

ssock = socket(AF_INET, SOCK_STREAM)
ssock.bind(ADDR)
ssock.listen(5)
csock = None

init()

while True:
#total_data = forward + backward + direction + breaker
	if csock is None:
		print("waiting for connection...")
		csock, addr_info = ssock.accept()
		print("got connection from", addr_info)
	else:
		total_data = csock.recv(BUFSIZE)
		total_data = total_data.decode()
		print(str(total_data))
		
		forward = total_data[0:2]
		backward = total_data[2:4]
		direction = total_data[4:6]
		breaker = total_data[6:8]
		velocity = total_data[8:10]#10 20 30

		if (forward == "+1") & (backward =="+1"):
			speed=20
			while (0 <= speed) & (speed <=30) :
				speed = speed - 5
				motor.setSpeed(speed)
				motor.forward()
				time.sleep(0.01)


		if (forward == "+1") & (backward == "00"):
			motor.setSpeed(velocity)
			motor.forward()

		if (forward == "00") & (backward =="+1"):
			motor.setSpeed(velocity)
			motor.backward()

		if breaker == "+1":
			motor.stop()

		if direction == "+3":
			servo_test.pwm.write(0, 0, 330)

		if direction == "+2":
			servo_test.pwm.write(0, 0, 300)

		if direction == "+1":
			servo_test.pwm.write(0, 0, 270)

		if direction == "00":
			servo_test.pwm.write(0, 0, 240)

		if direction == "-1":
			servo_test.pwm.write(0, 0, 210)

		if direction == "-2":
			servo_test.pwm.write(0, 0, 180)

		if direction == "-3":
			servo_test.pwm.write(0, 0, 150)


	#	else :
	#		raise(ValueError)

	#	time.sleep(0.01)