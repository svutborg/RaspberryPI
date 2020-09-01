import pigpio
import time
import math
from Tone import Tone

t = Tone(integer_frequencies = True)
print(t.tones)

def play_tone(pin, tone, duration):
    print(tone)
    pi.hardware_PWM(pin, t.tones[tone], 500000)
    time.sleep(duration/1000)
    pi.hardware_PWM(pin, 0, 500000)


pi = pigpio.pi()
#play_tone('A5', 0.2)
speakerPin = 13
c   = 'C4'
d   = 'D4'
e   = 'E4'
f   = 'F4'
g   = 'G4'
gS  = 'G#4'
a   = 'A4'
aS  = 'A#4'
b   = 'B4'
cH  = 'C5'
cSH = 'C#5'
dH  = 'D5'
dSH = 'D#5'
eH  = 'E5'
fH  = 'F5'
fSH = 'F#5'
gH  = 'G5'
gSH = 'G#5'
aH  = 'A5'

try:
    play_tone(speakerPin, a, 500)
    play_tone(speakerPin, a, 500)
    play_tone(speakerPin, a, 500)
    play_tone(speakerPin, f, 350)
    play_tone(speakerPin, cH, 150)

    play_tone(speakerPin, a, 500)
    play_tone(speakerPin, f, 350)
    play_tone(speakerPin, cH, 150)
    play_tone(speakerPin, a, 1000)
    #first bit

    play_tone(speakerPin, eH, 500)
    play_tone(speakerPin, eH, 500)
    play_tone(speakerPin, eH, 500)
    play_tone(speakerPin, fH, 350)
    play_tone(speakerPin, cH, 150)

    play_tone(speakerPin, gS, 500)
    play_tone(speakerPin, f, 350)
    play_tone(speakerPin, cH, 150)
    play_tone(speakerPin, a, 1000)
    #second bit...

    play_tone(speakerPin, aH, 500)
    play_tone(speakerPin, a, 350)
    play_tone(speakerPin, a, 150)
    play_tone(speakerPin, aH, 500)
    play_tone(speakerPin, gSH, 250)
    play_tone(speakerPin, gH, 250)

    play_tone(speakerPin, fSH, 125)
    play_tone(speakerPin, fH, 125)
    play_tone(speakerPin, fSH, 250)
    time.sleep(0.250)
    play_tone(speakerPin, aS, 250)
    play_tone(speakerPin, dSH, 500)
    play_tone(speakerPin, dH, 250)
    play_tone(speakerPin, cSH, 250)
    #start of the interesting bit

    play_tone(speakerPin, cH, 125)
    play_tone(speakerPin, b, 125)
    play_tone(speakerPin, cH, 250)
    time.sleep(0.250)
    play_tone(speakerPin, f, 125)
    play_tone(speakerPin, gS, 500)
    play_tone(speakerPin, f, 375)
    play_tone(speakerPin, a, 125)

    play_tone(speakerPin, cH, 500)
    play_tone(speakerPin, a, 375)
    play_tone(speakerPin, cH, 125)
    play_tone(speakerPin, eH, 1000)
    #more interesting stuff (this doesn't quite get it right somehow)

    play_tone(speakerPin, aH, 500)
    play_tone(speakerPin, a, 350)
    play_tone(speakerPin, a, 150)
    play_tone(speakerPin, aH, 500)
    play_tone(speakerPin, gSH, 250)
    play_tone(speakerPin, gH, 250)

    play_tone(speakerPin, fSH, 125)
    play_tone(speakerPin, fH, 125)
    play_tone(speakerPin, fSH, 250)
    time.sleep(0.250)
    play_tone(speakerPin, aS, 250)
    play_tone(speakerPin, dSH, 500)
    play_tone(speakerPin, dH, 250)
    play_tone(speakerPin, cSH, 250)
    #repeat... repeat

    play_tone(speakerPin, cH, 125)
    play_tone(speakerPin, b, 125)
    play_tone(speakerPin, cH, 250)
    time.sleep(0.250)
    play_tone(speakerPin, f, 250)
    play_tone(speakerPin, gS, 500)
    play_tone(speakerPin, f, 375)
    play_tone(speakerPin, cH, 125)

    play_tone(speakerPin, a, 500)
    play_tone(speakerPin, f, 375)
    play_tone(speakerPin, c, 125)
    play_tone(speakerPin, a, 1000)
finally:
    pi.hardware_PWM(speakerPin, 0, 500000)