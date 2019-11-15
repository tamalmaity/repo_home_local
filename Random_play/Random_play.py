import random
import winsound

frequency = 2000
duration = 500 # 1000ms = 1s

actual = random.randrange(1,100,1)
#print(actual)

tries = 0
guess = -1
while 1:
	guess = int(input("Enter your guess: "))
	tries += 1
	if (guess==actual):
		break
	elif (guess<actual):
		print("Your guessed number is smaller")
	else:
		print("Your guessed number is larger")
for i in range (1,5):
        winsound.Beep(frequency,duration)
print("Correct guess. Number of guesses used: ", tries)


