MedFreq
=======
Software for generating square waves via Raspberry PI GPIO pins.

Description
-----------
This is first release of the software, tested globaly - not detailed.
Idea behind the code is to read all illnesses with their medical frequencies from text file at once. Since they are read, system is converting the data to json object for futher usage. At the first stage software is configuring device GPIO outputs in total 10 items:

gpio_pin_numbers = [5, 6, 7, 13, 12, 16, 19, 20, 21, 26]

This GPIO pins are initialized with default values. When data and pins are reday, system is sending specyfied object (illness) found by it's name to the hardware process. Then all the defined frequencies are on output of the device at the same time for specyfied pins.
The default duty cycle is set to 50Hz

Example find illness and play it:
---------------------------------
illness_name = 'Wolfram Syndrome' - name of the illness to find

play(illnesses.get(illness_name)) - sending frequencies for specyfied illness to the device
