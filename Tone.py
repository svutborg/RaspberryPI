class Tone():

    tones = {}
    off_tone = {'off': 0}

    def __init__(self, octaves=8, integer_frequencies=False):
        import math
        tone_names = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        num_tones = len(tone_names)
        if integer_frequencies == True:
            for i in range(-9,octaves*num_tones,1):
                self.tones[tone_names[i%num_tones]+str((i+9)//num_tones)] = round(math.pow(2,(i-48)/12)*440.0)
        else:
            for i in range(-9,octaves*num_tones,1):
                self.tones[tone_names[i%num_tones]+str((i+9)//num_tones)] = math.pow(2,(i-48)/12)*440.0
        self.tones['off'] = 0