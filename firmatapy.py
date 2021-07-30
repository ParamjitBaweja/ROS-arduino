from pyfirmata import Arduino, util

import time


board = Arduino('/dev/ttyACM1')
#pin=board.get_pin('d:13:p')

while True:
	#for i in range(0,1):
		#pin.write(i)
		board.digital[13].write(1)
		#time.sleep(1)
	#for i in range(1,0):
		#pin.write(i)
		board.digital[13].write(0)
		#time.sleep(1)
		
		print(board.analog[1].read())
