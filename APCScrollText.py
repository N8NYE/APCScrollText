import mido
import time
import threading
from threading import Thread

####################################
#           config                 #
####################################
speed=.1
text='WORLD DOMINATION'

####################################



devices=mido.get_output_names()

for x in range(0, len(devices)):
	print str(x) + ":  " + devices[x]

x=input("Enter Output Device: ")
devicename=devices[x]
print devicename

outport=mido.open_output(devicename)
channel=8
#message='note_on channel='+str(channel)+' note='+str(note)+' velocity=127 time=0'


#Letters are mapped using midi messages aligned from the right side minus the note_on and note_off messages
#These will be added later to simplify the maps
class Letter:
	def __init__(self, chan):
		self.charList={
			'A':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=55 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=57 velocity=127 time=0'	
				],
			'B':	[

				],
			'C':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',

				'channel='+str(chan)+' note=57 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0'
				],
			'D':	[
				
				],
			'E':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',

				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=55 velocity=127 time=0',

				'channel='+str(chan)+' note=57 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0'
				],
			'F':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',

				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=55 velocity=127 time=0'
				],
			'G':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',

				'channel='+str(chan)+' note=57 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				],
			'H':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=57 velocity=127 time=0',

				'channel='+str(chan-3)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				],
			'I':	[
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=54 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=56 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',

				'channel='+str(chan)+' note=57 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',
				],
			'J':	[
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=54 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=56 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',

				'channel='+str(chan-3)+' note=57 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',
				],
			'K':	[

				],
			'L':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=57 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0'
				],
			'M':	[

				],
			'N':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan-3)+' note=54 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-1)+' note=56 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=57 velocity=127 time=0'
				],
			'0':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=57 velocity=127 time=0',

				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0'
				],
			'P':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',

				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=55 velocity=127 time=0',
				],
			'Q':	[

				],
			'R':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',

				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=55 velocity=127 time=0',
				],
			'S':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',

				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=55 velocity=127 time=0',

				'channel='+str(chan)+' note=57 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0'
				],
			'T':	[
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=54 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=56 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=53 velocity=127 time=0'
				],
			'U':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=57 velocity=127 time=0',

				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0'
				],
			'V':	[
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-1)+' note=56 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=56 velocity=127 time=0',
				'channel='+str(chan-3)+' note=55 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				],
			'W':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=54 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=56 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=57 velocity=127 time=0',

				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0',
				],
			'X':	[
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=54 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=57 velocity=127 time=0',
				'channel='+str(chan-1)+' note=56 velocity=127 time=0',
				'channel='+str(chan-3)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=53 velocity=127 time=0'
				
				],
			'Y':	[
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=54 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=56 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0'

				],
			'Z':	[
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=53 velocity=127 time=0'

				'channel='+str(chan)+' note=57 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0'

				
				'channel='+str(chan-1)+' note=54 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=56 velocity=127 time=0',
				
				],
			'O':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=57 velocity=127 time=0',

				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0'
				],
			'1':	[
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=54 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=56 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				],
			'2':	[

				],
			'3':	[
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=57 velocity=127 time=0',

				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',

				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',


				'channel='+str(chan)+' note=57 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0'
				],
			'4':	[

				],
			'5':	[

				],
			'6':	[

				],
			'7':	[

				],
			'8':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=57 velocity=127 time=0',

				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=55 velocity=127 time=0',
				'channel='+str(chan-2)+' note=55 velocity=127 time=0',
				'channel='+str(chan-3)+' note=55 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0'
				],
			'9':	[

				],
			'0':	[
				'channel='+str(chan-4)+' note=53 velocity=127 time=0',
				'channel='+str(chan-4)+' note=54 velocity=127 time=0',
				'channel='+str(chan-4)+' note=55 velocity=127 time=0',
				'channel='+str(chan-4)+' note=56 velocity=127 time=0',
				'channel='+str(chan-4)+' note=57 velocity=127 time=0',
				'channel='+str(chan)+' note=53 velocity=127 time=0',
				'channel='+str(chan)+' note=54 velocity=127 time=0',
				'channel='+str(chan)+' note=55 velocity=127 time=0',
				'channel='+str(chan)+' note=56 velocity=127 time=0',
				'channel='+str(chan)+' note=57 velocity=127 time=0',

				'channel='+str(chan-1)+' note=53 velocity=127 time=0',
				'channel='+str(chan-2)+' note=53 velocity=127 time=0',
				'channel='+str(chan-3)+' note=53 velocity=127 time=0',
				'channel='+str(chan-1)+' note=57 velocity=127 time=0',
				'channel='+str(chan-2)+' note=57 velocity=127 time=0',
				'channel='+str(chan-3)+' note=57 velocity=127 time=0'
				],
			' ':	[

				]
			


		}


def on(str):
	return 'note_on ' + str
def off(str):
	return 'note_off '+ str

#handles individual scrolling of a letter
def scrollLetter(pos, let):
	ogpos=pos
	while pos > -1:
		Char=Letter(pos)
		Char=Char.charList[let]
		for i in range(0, len(Char)):
			try:
				midi=mido.Message.from_str(on(Char[i]))
				outport.send(midi)
			except:
				pass 
		time.sleep(speed)
		for i in range(0, len(Char)):
			try:
				midi=mido.Message.from_str(off(Char[i]))
				outport.send(midi)
			except:
				pass 
		#time.sleep(speed)
		pos=pos-1

#handles scrolling of a lot of letters
def scrollMessage(mes):
	threads=[]
	for i in range(0, len(mes)):
		t=threading.Thread(target=scrollLetter, args=(12+(i*6), mes[i]))
		threads.append(t)
	for x in threads:
		x.start()
	for x in threads:
		x.join()
		
while True:
	scrollMessage(text)






