import RPi.GPIO as GPIO
import sys
from twython import Twython
import time

apiKey = ''
apiSecret = ''
accessToken = ''
accessTokenSecret = ''
api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)
auth = api.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
auth['auth_url']

while True:
	GPIO.setmode(GPIO.BCM)

	TRIG = 23 
	ECHO = 24

	print "Distance Measurement In Progress"

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG, False)
	print "Waiting For Sensor To Settle"
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	if distance < 20 :
		localtime = time.asctime( time.localtime(time.time()) )
		api.update_status(status = localtime + " [Knock, Knock! Someone is at home!][TwitterBot]")
		print "Tweet alert posted!"

	print "Distance:",distance,"cm"

	GPIO.cleanup()
