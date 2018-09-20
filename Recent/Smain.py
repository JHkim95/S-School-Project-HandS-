import servo_test
import motor
import socket
import time

def init():
    motor.setup()
    servo_test.setup()
    motor.setSpeed(0)
    servo_test.pwm.write(0,0,500)

HOST = "192.168.1.103"
PORT = 5050
BUFSIZE = 2
ADDR = (HOST, PORT)

ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssock.bind(ADDR)
ssock.listen(1)
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

		forward = total_data[0:1]
		#backward = total_data[1:2]
		direction = total_data[1:2]
		#breaker = total_data[6:8]
		#velocity = total_data[8:10] #10 20 30

		#if (forward == "+1") & (backward =="+1"):
		#	speed=20
		#	while (0 <= speed) & (speed <=30) :
		#		speed = speed - 5
		#		motor.setSpeed(speed)
		#		motor.forward()
		#		time.sleep(0.01)


		if (forward == "3") :   
			speed = 40
			motor.setSpeed(speed)
			motor.forward()

		if (forward == "2") :   
			speed = 20
			motor.setSpeed(speed)
			motor.forward()

		if (forward =="1"):
			speed = 20
			motor.setSpeed(speed)
			motor.backward()

		if (forward == "0") :   
			speed = 40
			motor.setSpeed(speed)
			motor.backward()

		if forward == "4":
			motor.stop()

		if direction == "4":
			servo_test.pwm.write(0, 0, 300)

		if direction == "3":
			servo_test.pwm.write(0, 0, 400)

		if direction == "2":
			servo_test.pwm.write(0, 0, 500)

		if direction == "1":
			servo_test.pwm.write(0, 0, 600)

		if direction == "0":
			servo_test.pwm.write(0, 0, 700)


#		else :
#			raise(ValueError)

#		time.sleep(0.01)
