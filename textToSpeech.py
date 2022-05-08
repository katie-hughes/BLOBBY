import time
import random
import subprocess


def play(name):
	subprocess.Popen(['mpg123', '-q', 'audio_files/BLOBBY'+name+'.mp3']).wait()


print("BLOBBY!!\n")
while(True):
	print("\nPlease input your text!")
	txt = input()
	spl = txt.split()
	nwords = len(spl)
	for word in spl:
		word = word.lower()
		sleep_time = 0
		if "bye" in word:
			play('Bye')
		elif "hello" in word:
			play("Hello")
		elif "hmm" in word:
			play("Hmm")
		elif "oh" in word:
			play("Oh")
		elif "reee" in word:
			play("Reee")
		elif "sorry" in word:
			play("Sorry")
		elif "thank" in word:
			play("Thank")
		elif "um" in word:
			play("Um")
		elif "what" in word:
			play("What")
		elif "yeah" in word:
			play("Yeah")
		elif "you" in word:
			play("You")
		elif "!" in word:
			play("Exclaim")
		else:
			play(str(random.randint(1,4)))

		if ('.' in word) or ('!' in word):
			## end of sentance
			sleep_time = 0.3

		time.sleep(sleep_time)
	print()
