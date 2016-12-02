#!/usr/bin/python
from decimal import Decimal
import json
from tools import HasStringNumbers
from time import sleep
import RPi.GPIO as GPIO

gpio_pin_numbers = [5, 6, 7, 13, 12, 16, 19, 20, 21, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_numbers, GPIO.OUT)

gpio_objects = []

class IllnessItem:
    def __init__(self, name, frequencies, fill_time):
        self.name = name
        self.frequencies = frequencies
        self.fill_time = fill_time

class Illnesses:

	illnesses_file_path = 'frequencies.txt'

	def __init__(self, illnesses=None):
		self.illnesses = illnesses or []

	def add(self, name, frequencies, fill_time):
		# add new item to collection
		item = IllnessItem(name, frequencies, fill_time)
		self.illnesses.append(item)
		return item

	def load(self):
		# load illnesses with frequencies from external txt file
		with open(self.illnesses_file_path) as f:
			content = f.readlines()
			for i in content:
				frequencies_decimal = []
				if len(i) > 2:
					try:
						split = i.split(":")
						name = split[0]
						if HasStringNumbers(str(split)):
							frequencies = split[1].split(",")
							if len(frequencies) == 10:
								for i in frequencies:
									frequencies_decimal.append(str(Decimal(i)))
								self.add(name, frequencies_decimal, 50)
					except Exception:
						pass

	def get(self, name):
		# get specyfied illness base on name
		return [x for x in self.illnesses if x.name == name][0]

	def write(self):
		# write to json file
	    jsn = json.dumps(self, default=lambda o: o.__dict__,
	                     sort_keys=True, indent=4)
	    open('jsn_out.json', 'w').write(jsn)

	def read(self):
		# read from json file
	    f = open('jsn_out.json', 'r').read()
	    jsn = json.loads(f)
	    return jsn


def play(illness):
	# play specyfied illness frequencies
	for i, frequency in enumerate(illness.frequencies):
		gpio_obj = gpio_objects[i]
		gpio_obj.ChangeFrequency(Decimal(frequency))
		gpio_obj.start(illness.fill_time)
	
def stop():
	# stop playing frequencies and release resources
	GPIO.cleanup()

# initialize all gpio objects
for i, pin in enumerate(gpio_pin_numbers):
	obj = GPIO.PWM(pin, 1)
	gpio_objects.append(obj)

illnesses = Illnesses()
illnesses.load()
illness_name = 'Wolfram Syndrome'
play(illnesses.get(illness_name))
raw_input("Press Enter to Stop")
stop()