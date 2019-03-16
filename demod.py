import sys
from aubio import source, pitch
import numpy as np
import re
import pyaudio
import wave

print("Type in the number of seconds of tape to be read.")
x = input()
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = x
WAVE_OUTPUT_FILENAME = "tape_input.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* reading from tape")

frames = []

for i in range(0, int(RATE / int(CHUNK) * int(RECORD_SECONDS))):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done reading")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


win_s = 4096
hop_s = 512

s = source("tape_input.wav", 44100, hop_s)
samplerate = s.samplerate

tolerance = 0.8

pitch_o = pitch("yin", win_s, hop_s, samplerate)
pitch_o.set_unit("midi")
pitch_o.set_tolerance(tolerance)

pitches = []
confidences = []

total_frames = 0
while True:
    samples, read = s()
    pitch = pitch_o(samples)[0]
    pitches += [pitch]
    confidence = pitch_o.get_confidence()
    confidences += [confidence]
    total_frames += read
    if read < hop_s: break


#print("Average frequency = " + str(np.array(pitches).mean()) + " hz")

numbers = []
for x in pitches:
    if int(x) in range (62, 63):
        numbers.append("0")
    elif int(x) in range (73, 74):
        numbers.append("1")
    elif int(x) in range (78, 82):
        numbers.append("2")
    elif int(x) in range (84, 87):
        numbers.append("3")
    elif int(x) in range (88, 89):
        numbers.append("4")
    elif int(x) in range (91, 92):
        numbers.append("5")
    elif int(x) in range (94, 95):
        numbers.append("6")
    elif int(x) in range (96, 97):
        numbers.append("7")
    elif int(x) in range (98, 99):
        numbers.append("8")
    elif int(x) in range (100, 101):
        numbers.append("9")
    elif int(x) == 102:
        numbers.append("NULL")
    elif int(x) >= 103:
        numbers.append("STREAM_CAP")

print(pitches)

aux_list = []
for i in range(len(numbers)):
    if not numbers[i] == numbers[i-1]:
        aux_list.append(numbers[i])

#print(aux_list)

interpret = ''.join(aux_list)

#print(interpret)

text_chunks = interpret.split("ULL")

#print(text_chunks)

output = []

def ascii_to_char(text):
    space = re.search('032N', text)
    exclm = re.search('03N',  text)
    dblqt = re.search('034N', text)
    hshtg = re.search('035N', text)
    dollr = re.search('036N', text)
    perid = re.search('046N', text)
    comma = re.search('04N',  text)
    A = re.search('065N', text)
    B = re.search('06N', text)
    C = re.search('067N', text)
    D = re.search('068N', text)
    E = re.search('069N', text)
    F = re.search('070N', text)
    G = re.search('071N', text)
    H = re.search('072N', text)
    I = re.search('073N', text)
    J = re.search('074N', text)
    K = re.search('075N', text)
    L = re.search('076N', text)
    M = re.search('07N', text)
    N = re.search('078N', text)
    O = re.search('079N', text)
    P = re.search('080N', text)
    Q = re.search('081N', text)
    R = re.search('082N', text)
    S = re.search('083N', text)
    T = re.search('084N', text)
    U = re.search('085N', text)
    V = re.search('086N', text)
    W = re.search('087N', text)
    X = re.search('08N', text)
    Y = re.search('089N', text)
    Z = re.search('090N', text)

    if space:
        output.append(' ')
    if exclm:
        output.append('!')
    if dblqt:
        output.append('"')
    if hshtg:
        output.append('#')
    if dollr:
        output.append('$')
    if perid:
        output.append('.')
    if comma:
        output.append(',')
    if A:
        output.append('A')
    if B:
        output.append('B')
    if C:
        output.append('C')
    if D:
        output.append('D')
    if E:
        output.append('E')
    if F:
        output.append('F')
    if G:
        output.append('G')
    if H:
        output.append('H')
    if I:
        output.append('I')
    if J:
        output.append('J')
    if L:
        output.append('L')
    if M:
        output.append('M')
    if O:
        output.append('O')
    if P:
        output.append('P')
    if Q:
        output.append('Q')
    if R:
        output.append('R')
    if S:
        output.append('S')
    if T:
        output.append('T')
    if U:
        output.append('U')
    if V:
        output.append('V')
    if W:
        output.append('W')
    if X:
        output.append('X')
    if Y:
        output.append('Y')
    if Z:
        output.append('Z')



for x in text_chunks:
    ascii_to_char(x)

print(''.join(output))
