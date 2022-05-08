import time
import random
import subprocess


def play(name):
	subprocess.Popen(['mpg123', '-q', 'audio_files/BLOBBY'+name+'.mp3']).wait()


print("BLOBBY!!\n")
while(True):
	txt = input("\nPlease input your text!\n")
	spl = txt.split()
	nwords = len(spl)
	for word in spl:
		if ('.' in word):
			## end of sentance
			print("BLOBBY.", end=' ')
			play(str(random.randint(1,4)))
			time.sleep(0.3)
		elif ('!' in word):
			## end of sentance
			print("BLOBBY!!!", end=' ')
			play('Exclaim')
			time.sleep(0.3)
		else:
			print('BLOBBY', end=' ')
			play(str(random.randint(1,4)))
			time.sleep(0.05)
	print()
