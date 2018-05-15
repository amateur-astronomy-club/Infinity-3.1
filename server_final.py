from flask import Flask
import sys
import time
import RPi.GPIO as GPIO
#from wsgiserver import WSGIServer

# monkey.patch_all(aggressive=False)
app = Flask(__name__)
 
@app.route("/forward/<float:speed>")
def forward(speed):
	GPIO.output(p18,GPIO.LOW)
	GPIO.output(p22,GPIO.LOW)
	GPIO.output(p15, GPIO.HIGH)
	GPIO.output(p12, GPIO.HIGH)
	GPIO.output(p13, GPIO.HIGH)
	print("Forward")
	print "Speed value is %f" %(speed)
	if speed >=0:
		speed=speed*100
		speed="%3.0f" %speed
		speed=int(speed)
		pwm.ChangeDutyCycle(speed)
		
	return "Forward"

@app.route("/backward/<float:speed>")
def backward(speed):
	GPIO.output(p15,GPIO.LOW)
	GPIO.output(p12,GPIO.LOW)
	GPIO.output(p18, GPIO.HIGH)
	GPIO.output(p22, GPIO.HIGH)
	GPIO.output(p13, GPIO.HIGH)

	print("Back")
	print "Speed value is %f" %(speed)
	if speed >=0:
		speed=speed*100
		speed="%3.0f" %speed
		speed=int(speed)
		pwm.ChangeDutyCycle(speed)
	
	return "Back"

@app.route("/left/<float:speed>")
def left(speed):
	GPIO.output(p15,GPIO.LOW)
	GPIO.output(p22,GPIO.LOW)
	GPIO.output(p12, GPIO.HIGH)
	GPIO.output(p18, GPIO.HIGH)
	GPIO.output(p13, GPIO.HIGH)
	print("left")
	print "Speed value is %f" %(speed)
	if speed >=0:
		speed=speed*100
		speed="%3.0f" %speed
		speed=int(speed)
		pwm.ChangeDutyCycle(speed)
	return "left"

@app.route("/right/<float:speed>")
def right(speed):
	GPIO.output(p18,GPIO.LOW)
	GPIO.output(p12,GPIO.LOW)
	GPIO.output(p15, GPIO.HIGH)
	GPIO.output(p22, GPIO.HIGH)
	GPIO.output(p13, GPIO.HIGH)
	print("right")
	print "Speed value is %f" %(speed)
	if speed >=0:
		speed=speed*100
		speed="%3.0f" %speed
		speed=int(speed)
		pwm.ChangeDutyCycle(speed)
	return "right"


@app.route("/stop")
def stop():
	GPIO.output(p15, GPIO.LOW)
	GPIO.output(p18, GPIO.LOW)
	GPIO.output(p12, GPIO.LOW)
	GPIO.output(p22, GPIO.LOW)
	GPIO.output(p13, GPIO.LOW)

	print("stop")
	return "stop"
 
@app.route("/test")
def test():
	GPIO.output(p13, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(p13, GPIO.LOW)
	time.sleep(2)
	# GPIO.cleanup()
	print("Test Successful!")
	return "Test Successful"

if __name__ == "__main__":
	mode=GPIO.getmode()

	GPIO.cleanup()
	
	p15 = 22    #GPIO22
	p18 = 24    #GPIO24
	p12 = 18    #GPIO18
	p22 = 25    #GPIO25
	p13 = 27   #GPIO27  This is working, this pin we will use as enable pin(a common enable pin for all the motors)



	GPIO.setmode(GPIO.BCM) 
	# GPIO.setmode(GPIO.BOARD)
	GPIO.setup(p15, GPIO.OUT)
	GPIO.setup(p18, GPIO.OUT)
	GPIO.setup(p12, GPIO.OUT)
	GPIO.setup(p22, GPIO.OUT)
	GPIO.setup(p13, GPIO.OUT)
	#GPIO.cleanup()

	pwm=GPIO.PWM(p13, 100) #Configuring enable pin i.e GPIO26 for pwm with frequency 100Hz
	pwm.start(50)         #Starting with 50% duty cycle

		
	app.run(host="0.0.0.0", port=8002);
	#http_server = WSGIServer(app)
	#_server.serve_forever()