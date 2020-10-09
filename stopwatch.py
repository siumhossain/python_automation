import time 

print('press enter for start and cntrl+c for stop')


input()


print('start')


startTime = time.time()
lastTime = startTime

lapNum = 1

try:
	while True:
		input()
		lapTime = round(time.time() - lastTime,3)
		totalTime = round(time.time() - startTime,3)
		print('lap #%s:%s (%s)'%(lapNum,totalTime,lastTime),end='')
		lapNum += 1 
		lastTime = time.time()
except KeyboardInterrupt:
	print('\nDone')