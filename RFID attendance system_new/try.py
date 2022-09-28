import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
reader = SimpleMFRC522()
id, text = reader.read()
print(id)
print(type(id))
print(text)
sleep(2)





