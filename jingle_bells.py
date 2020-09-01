import time
import pigpio

buzzerPin = 13
tempo = 0.1
notes = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'g', 'c', 'd', 'e', ' ', 'f', 'f', 'f', 'f', 'f', 'e', 'e', 'e', 'e', 'd', 'd', 'e', 'd', 'g']
duration = [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]

def playTheTone(note, duration):
    notesName = [ 'c', 'd', 'e', 'f', 'g' ]
    tones = [ 261, 293, 329, 349, 392 ]

    for i in range(len(tones)):
        if note == notesName[i]:
            pi.hardware_PWM(buzzerPin, tones[i], 500000)
            time.sleep(duration)
            pi.hardware_PWM(buzzerPin, 0, 500000)



pi = pigpio.pi()

for i in range(len(notes)):
    if (notes[i] == ' '):
        time.sleep(duration[i] * tempo)
    else:
        playTheTone(notes[i], duration[i] * tempo)
    time.sleep((tempo*2)*duration[i])
print("done")
pi.hardware_PWM(buzzerPin, 0, 500000)