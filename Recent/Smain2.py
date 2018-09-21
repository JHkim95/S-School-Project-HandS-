import servo_test
import motor
import socket
import time
import sys

def init():
    motor.setup()
    servo_test.setup()
    motor.setSpeed(0)
    servo_test.pwm.write(0,0,500)

HOST = "192.168.0.6"
PORT = 5333
BUFSIZE = 2
ADDR = (HOST, PORT)

ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssock.bind(ADDR)
ssock.listen(0)
csock = None

init()
try :
	while True:
		if csock is None:
			print("Waiting for connection...")
			csock, addr_info = ssock.accept()
			print("Get connection from", addr_info)
		else:
			total_data = csock.recv(BUFSIZE)
			total_data = total_data.decode()

			forward = total_data[0]
			direction = total_data[1]

			if (forward == "3") :
				speed = 35
				motor.setSpeed(speed)
				motor.forward()

			elif (forward == "2") :
				speed = 25
				motor.setSpeed(speed)
				motor.forward()

			elif (forward =="1"):
				speed = 25
				motor.setSpeed(speed)
				motor.backward()

			elif (forward == "0") :
				speed = 30
				motor.setSpeed(speed)
				motor.backward()

			elif forward == "4":
				motor.stop()

			elif forward == "5":
				motor.stop()


				
			if direction == "0":
				servo_test.pwm.write(0, 0, 330)

			elif direction == "1":
				servo_test.pwm.write(0, 0, 400)

			elif direction == "2":
				servo_test.pwm.write(0, 0, 500)

			elif direction == "3":
				servo_test.pwm.write(0, 0, 550)

			elif direction == "4":
				servo_test.pwm.write(0, 0, 700)

except KeyboardInterrupt:
	pass

print("\n STOP!")
sys.exit(1)
